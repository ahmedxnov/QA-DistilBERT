from transformers.pipelines import QuestionAnsweringPipeline
from .config import DEFAULT_BATCH_SIZE

# def make_predictions_sequential(data : dict, question_answerer : QuestionAnsweringPipeline) -> dict:
#     predictions = dict()
#     for article in data["data"]:
#         for paragraph in article["paragraphs"]:
#             for qa in paragraph["qas"]:
#                 predictions[qa["id"]] = question_answerer(question=qa["question"], context=paragraph["context"])["answer"]
#     return predictions

def make_batch_predictions(data : dict, question_answerer : QuestionAnsweringPipeline, batch_size : int = DEFAULT_BATCH_SIZE) -> dict:
    all_items = list()
    for article in data["data"]:
        for paragraph in article["paragraphs"]:
            for qa in paragraph["qas"]:
                all_items.append((qa["id"], qa["question"], paragraph["context"]))
    
    predictions = dict()
    
    for i in range(0, len(all_items), batch_size):
        batch = all_items[i:i+batch_size]
        questions = [item[1] for item in batch]
        contexts = [item[2] for item in batch] 
        
        # Batch inference
        results = question_answerer(question=questions, context=contexts)
        if not isinstance(results, list):
            results = [results]
            
        for item, result in zip(batch, results):
            predictions[item[0]] = result["answer"]

    return predictions