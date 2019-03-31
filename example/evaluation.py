"""
Part of the evaluation code was copied from the
https://github.com/allenai/bi-att-flow/blob/master/squad/evaluate-v1.1.py
"""

from collections import Counter
import json
import re
import string
import os

from allennlp.predictors.predictor import Predictor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

from wildnlp.aspects import QWERTY, RemoveChar
from wildnlp.datasets import SQuAD


def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def f1_score(prediction, ground_truth):
    prediction_tokens = normalize_answer(prediction).split()
    ground_truth_tokens = normalize_answer(ground_truth).split()
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return 0
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1


def metric_max_over_ground_truths(metric_fn, prediction, ground_truths):
    scores_for_ground_truths = []
    for ground_truth in ground_truths:
        score = metric_fn(prediction, ground_truth)
        scores_for_ground_truths.append(score)
    return max(scores_for_ground_truths)


def calculate_dataset_scores(dataset, predict_func, score_func):

    scores = []
    for entry in dataset:
        for paragraph in entry['paragraphs']:
            context = paragraph['context']
            for qa in paragraph['qas']:
                gt_answers = [answer['text'] for answer in qa['answers']]
                prediction = predict_func(context, qa['question'])
                scores.append(metric_max_over_ground_truths(score_func,
                                                            prediction,
                                                            gt_answers))
    return scores


def download_squad(filename):
    if not os.path.isfile(filename):
        print("Downloading SQuAD datataset.")
        data = requests.get(
            'https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json')

        with open(filename, 'w') as f:
            json.dump(data.json(), f)


def create_log_output(mean_scores, severity):

    output = dict()
    output['f1_mean'] = np.mean(mean_scores)
    output['f1_std'] = np.std(mean_scores)
    output['severity'] = severity

    return output


def evaluate(squad_obj, score_func, predict_func, aspect):

    f1_original =\
        calculate_dataset_scores(squad_obj.data['data'],
                                 predict_func, score_func)
    means = [np.mean(f1_original)]
    results = [create_log_output(means, 0)]

    for severity in range(10, 101, 10):
        try:
            aspect_obj = aspect(words_percentage=severity)
            means = []
            for _ in range(10):
                modified = squad_obj.apply(aspect_obj)
                f1_scores = calculate_dataset_scores(modified['data'],
                                                     predict_func,
                                                     score_func)
                means.append(np.mean(f1_scores))

            results.append(create_log_output(means, severity))

        except KeyboardInterrupt:
            break

        except:
            pass

    return results


def save_plot(main_results, main_results_label,
              comparison_results, comparison_results_label,
              fig_name, suptitle, title):
    plt.figure(figsize=(10, 5))
    plt.errorbar(x=list(range(len(main_results))),
                 y=main_results['f1_mean'],
                 yerr=main_results['f1_std'],
                 marker='o',
                 label=main_results_label)
    plt.errorbar(x=list(range(len(comparison_results))),
                 y=comparison_results['f1_mean'],
                 marker='^',
                 label=comparison_results_label,
                 linestyle='dashed')
    plt.legend()
    plt.suptitle(suptitle)
    plt.title(title)
    plt.ylabel('F1 score')
    plt.xlabel('Severity (% of words corrupted)')
    plt.grid(False)
    plt.xticks(list(range(len(main_results))), main_results['severity'])
    plt.show()
    plt.savefig(fig_name)


if __name__ == '__main__':

    BiDAF = Predictor.from_path(
        "https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

    def bidaf_predict(context, question):
        return BiDAF.predict(passage=context,
                             question=question)['best_span_str']

    download_squad('dev-v1.1.json')

    squad = SQuAD()
    squad.load('dev-v1.1.json')

    evaluation_remove_char = evaluate(squad, f1_score, bidaf_predict, RemoveChar)
    evaluation_remove_qwerty = evaluate(squad, f1_score, bidaf_predict, QWERTY)

    remove_char_df = pd.DataFrame(evaluation_remove_char,
                                  columns=['severity', 'f1_mean', 'f1_std'])
    qwerty_df = pd.DataFrame(evaluation_remove_qwerty,
                                  columns=['severity', 'f1_mean', 'f1_std'])

    remove_char_df.to_csv('remove_char.csv')
    qwerty_df.to_csv('qwerty.csv')

    save_plot(remove_char_df, 'RemoveChar', qwerty_df, 'QWERTY',
              'remove_char', 'Analysis of BiDAF robustness to characters removal',
              'QWERTY for comparison')

    save_plot(qwerty_df, 'QWERTY', remove_char_df, 'RemoveChar',
              'qwerty', 'Analysis of BiDAF robustness to QWERTY misspellings',
              'RemoveChar for comparison')
