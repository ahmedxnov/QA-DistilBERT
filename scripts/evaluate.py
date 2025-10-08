from src.model import load_QA_answerer
from src.data_loader import load_data
from src.inference import make_batch_predictions
from src.metrics import compute_score

def main():
    data = load_data()
    question_answerer = load_QA_answerer()
    predictions = make_batch_predictions(data, question_answerer)  # Now uses DEFAULT_BATCH_SIZE=32
    print(compute_score(data["data"], predictions))
    
if __name__ == "__main__":
    main()
    