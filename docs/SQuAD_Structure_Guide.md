# SQuAD v1.1 Dataset Structure Guide

## 📊 Hierarchical Structure with Data Types

```
dev-v1.1.json
├── version: str = "1.1"
└── data: List[Dict] = [48 articles]
    └── article: Dict
        ├── title: str = "Super_Bowl_50"
        └── paragraphs: List[Dict] = [54 paragraphs]
            └── paragraph: Dict
                ├── context: str = "Super Bowl 50 was an American football game..."
                └── qas: List[Dict] = [30 questions]
                    └── qa: Dict
                        ├── id: str = "56be4db0acb8001400a502ec"
                        ├── question: str = "Which NFL team represented the AFC?"
                        └── answers: List[Dict] = [3 answers]
                            └── answer: Dict
                                ├── text: str = "Denver Broncos"
                                └── answer_start: int = 177
```

## 🔍 Detailed Field Types & Descriptions

### **Root Level** (`Dict`)
- **`version`**: `str` - Dataset version identifier (e.g., "1.1")
- **`data`**: `List[Dict]` - Array of articles covering different topics

### **Article Level** (`Dict`)
- **`title`**: `str` - Article/topic title, often Wikipedia article name
- **`paragraphs`**: `List[Dict]` - Paragraphs belonging to this article

### **Paragraph Level** (`Dict`)
- **`context`**: `str` - Text passage (50-800+ chars) containing answers
- **`qas`**: `List[Dict]` - Questions that can be answered from this context

### **QA Level** (`Dict`)
- **`id`**: `str` - Unique identifier (format: alphanumeric hash)
- **`question`**: `str` - Natural language question about the context
- **`answers`**: `List[Dict]` - Multiple human annotations (typically 3-5)

### **Answer Level** (`Dict`)
- **`text`**: `str` - Answer span extracted from context
- **`answer_start`**: `int` - Zero-based character index where answer begins

## ⚠️ Type Constraints & Validation Rules

| Field | Type | Constraints |
|-------|------|-------------|
| `answer_start` | `int` | Must be ≥ 0 and < `len(context)` |
| `text` | `str` | Must match `context[answer_start:answer_start+len(text)]` |
| `id` | `str` | Must be unique across entire dataset |
| `answers` | `List[Dict]` | Minimum 1 answer, typically 3-5 annotations |
| `context` | `str` | Usually 50-800 characters, can be longer |
| `question` | `str` | Natural language, typically ends with '?' |
| `title` | `str` | Wikipedia article titles, may contain underscores |