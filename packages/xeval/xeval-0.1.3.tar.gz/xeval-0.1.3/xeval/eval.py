from xeval.metric import Metrics
from xspike import Result, Logger
from datasets import Dataset
import pandas as pd
from rich.console import Console
from rich.table import Table
from typing import Union

log = Logger(__name__) 

def eval(eval_inputs: Union[Dataset, pd.DataFrame, dict] = None, 
                     metrics: list = [], 
                     device: int = 0,
                     addon_metrics: dict = None,
                     ):
    """计算评价指标，目前已支持的指标有: corpus_bleu, sent_bleu, sent_sacrebleu, corpus_sacrebleu, meteor, rouge, bertscore, chrf, dist, f1_nlp, f1_space
    
    addon_metrics 是一个字典，可以添加自定义的评价指标。
    自定义的评价指标需要继承 xeval.metric.MetricCritic 类，并实现 score 方法。
    
    class SacreSentenceBleuCriticInside:
        def __init__(self) -> None:
            self.name = "sacrebleu_sent"

        def score(self, candidates: list[str], references: list[str], eval_result: xspike.Result, *args, **kwargs) -> xspike.Result:
            bleu = []
            for i, a_gold in enumerate(references):
                bleu.append(sacrebleu.corpus_bleu([candidates[i]], [[a_gold]]).score)
            bleu_score = round(mean(bleu), 4)
            eval_result.add(sacrebleu_sent=bleu_score)
            return eval_result

    Args:
        eval_inputs (Union[Dataset, pd.DataFrame, dict], optional): _description_. Defaults to None.
        metrics (list, optional): _description_. Defaults to [].
        device (int, optional): _description_. Defaults to 0.
        addon_metrics (dict, optional): _description_. Defaults to None.
    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if addon_metrics is not None:
        for k, v in addon_metrics.items():
            if k in Metrics:
                log.warning("评价指标 {} 已存在，将覆盖原有指标。".format(k))
            Metrics[k] = v
    
    if not isinstance(eval_inputs, Dataset):
        if isinstance(eval_inputs, pd.DataFrame):
            eval_inputs = Dataset.from_pandas(eval_inputs)
        elif isinstance(eval_inputs, dict):
            eval_inputs = Dataset.from_dict(eval_inputs)
        else:
            raise ValueError("评价指标计算的输入 eval_inputs 必须是 Dataset, pd.DataFrame 或者 dict类型，并满足转为 Dataset 的条件。")
    eval_result = Result()
    if "model_responses" in eval_inputs.column_names:
        model_responses = eval_inputs["model_responses"]
    else:
        model_responses = eval_inputs["generated"]
    if "references" in eval_inputs.column_names:
        references = eval_inputs["references"]
    else:
        return eval_result
    
    if "" in model_responses:
        log.warning("评价指标计算的输入中（model_responses）包含空值，评测结果或有偏颇。")
        
    
    for metric in metrics:
        if metric not in Metrics:
            log.warning("评价指标 {} 不在可用的评价指标列表中，将跳过该指标。".format(metric))
            continue
        
        log.info("计算 {} 评价指标...".format(metric))
        
        try:
            eval_result = Metrics[metric].score(candidates=model_responses, references=references, eval_result=eval_result, device=device, eval_dataset=eval_inputs)
        except Exception as e:
            log.error(e)
            log.warning("评价指标 {} 计算失败，将跳过该指标。".format(metric))

    console = Console(color_system="256", style="cyan")
    table = Table(style="cyan", show_footer=False, title="[bold green]Evaluation results")
    table.add_column("Metric", justify="right", style="magenta")
    table.add_column("Score :yum:", justify="left", style="magenta")
    for k, v in eval_result.items():
        table.add_row(k, str(v))
    console.print(table)
    
    return eval_result