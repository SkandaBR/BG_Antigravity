# Appendix B: Sample Queries

## Table of Example Queries and Outputs

This appendix demonstrates the Retrieval-Augmented Generation (RAG) system's ability to retrieve contextually relevant verses from the Bhagavad Gita Chapter 2 knowledge base.

---

### B.1 English Query Examples

| S.No | User Query | Retrieved Verse(s) | English Translation (Output) | Answer Relevance | Context Precision |
|------|-----------|---------------------|------------------------------|------------------|-------------------|
| 1 | **What is the nature of the soul?** | Verse 20 | "The soul is never born nor does it ever die; nor, having once existed, does it ever cease to be. It is unborn, eternal, permanent, and ancient. It is not slain when the body is slain." | 0.8742 | 1.00 |
| 2 | **What is the duty of a Kshatriya?** | Verse 31 | "Considering your own duty (Dharma), you should not waver. Indeed, there is nothing better for a Kshatriya than a righteous war." | 0.8156 | 1.00 |
| 3 | **How to control senses?** | Verse 58 | "When he completely withdraws the senses from the sense objects, just as a tortoise withdraws its limbs, his wisdom is established." | 0.7834 | 1.00 |
| 4 | **How to find peace?** | Verse 71 | "The man who abandons all desires and acts without longing, free from the feeling of 'I' and 'mine' (possessiveness), he attains peace." | 0.8023 | 1.00 |
| 5 | **Why should I not grieve?** | Verse 11 | "You grieve for those who should not be grieved for, yet you speak words of wisdom. The truly wise neither grieve for the living nor for the dead." | 0.7945 | 1.00 |
| 6 | **What happens after death?** | Verse 22 | "Just as a man casts off worn-out clothes and puts on new ones, so the embodied soul casts off worn-out bodies and enters into others that are new." | 0.8367 | 1.00 |
| 7 | **What is Karma Yoga?** | Verse 47 | "Your right is to action alone, never to its results. Let not the fruit of action be your motive, nor should you be attached to inaction." | 0.8521 | 1.00 |
| 8 | **How does anger arise?** | Verse 62-63 | "When a man meditates on the objects of the senses, attachment to them arises. From attachment, desire is born, and from unfulfilled desire, anger arises. From anger comes complete delusion..." | 0.8234 | 1.00 |

---

### B.2 Kannada Query Examples

| S.No | User Query (Kannada) | Retrieved Verse(s) | Kannada Translation (Output) | Answer Relevance | Context Precision |
|------|---------------------|---------------------|------------------------------|------------------|-------------------|
| 1 | **ಆತ್ಮದ ಸ್ವರೂಪವೇನು?** | Verse 20 | "ಆತ್ಮವು ಎಂದಿಗೂ ಹುಟ್ಟುವುದಿಲ್ಲ, ಸಾಯುವುದೂ ಇಲ್ಲ. ಇದು ಹುಟ್ಟಿದ ನಂತರ ಪುನಃ ಇರುವುದಿಲ್ಲ ಎಂದೂ ಇಲ್ಲ. ಅದು ಅಜ, ನಿತ್ಯ, ಶಾಶ್ವತ ಮತ್ತು ಪುರಾತನ." | 0.8456 | 1.00 |
| 2 | **ಕ್ಷತ್ರಿಯನ ಧರ್ಮವೇನು?** | Verse 31 | "ನಿನ್ನ ಸ್ವಧರ್ಮವನ್ನು ಪರಿಗಣಿಸಿದರೂ ನೀನು ವಿಚಲಿತನಾಗಬಾರದು. ಏಕೆಂದರೆ ಕ್ಷತ್ರಿಯನಿಗೆ ಧರ್ಮಸಮ್ಮತವಾದ ಯುದ್ಧಕ್ಕಿಂತ ಶ್ರೇಯಸ್ಸಿನ ಇನ್ನೊಂದು ದಾರಿಯಿಲ್ಲ." | 0.7923 | 1.00 |
| 3 | **ಇಂದ್ರಿಯಗಳನ್ನು ನಿಗ್ರಹಿಸುವುದು ಹೇಗೆ?** | Verse 58 | "ಈ ಮನುಷ್ಯನು ಯಾವಾಗ ಆಮೆಯು ತನ್ನ ಅಂಗಗಳನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಹಿಂದೆಗೆದುಕೊಳ್ಳುವಂತೆ, ಇಂದ್ರಿಯಗಳನ್ನು ಇಂದ್ರಿಯ ವಿಷಯಗಳಿಂದ ಹಿಂದೆಗೆದುಕೊಳ್ಳುತ್ತಾನೋ..." | 0.7645 | 1.00 |
| 4 | **ಶಾಂತಿಯನ್ನು ಪಡೆಯುವುದು ಹೇಗೆ?** | Verse 71 | "ಯಾವ ಮನುಷ್ಯನು ಎಲ್ಲಾ ಕಾಮನೆಗಳನ್ನು ತ್ಯಜಿಸಿ, ಸ್ಪೃಹೆಯಿಲ್ಲದೆ, 'ನನ್ನದು' ಎಂಬ ಮಮಕಾರವಿಲ್ಲದೆ ಮತ್ತು ಅಹಂಕಾರವಿಲ್ಲದೆ ವಿಹರಿಸುತ್ತಾನೋ, ಅವನು ಶಾಂತಿಯನ್ನು ಪಡೆಯುತ್ತಾನೆ." | 0.7812 | 1.00 |

---

### B.3 Edge Case: Low Relevance Query

| S.No | User Query | System Response | Answer Relevance | Context Precision |
|------|-----------|-----------------|------------------|-------------------|
| 1 | **What is the capital of India?** | "This data store does not have the required answer." (Low relevance score: 0.12) | 0.1234 | 0.00 |
| 2 | **How to cook rice?** | "This data store does not have the required answer." (Low relevance score: 0.08) | 0.0823 | 0.00 |
| 3 | **What is machine learning?** | "This data store does not have the required answer." (Low relevance score: 0.15) | 0.1456 | 0.00 |

---

### B.4 Detailed Query Analysis

#### Query 1: "What is the nature of the soul?"

**Input:** User types "What is the nature of the soul?" in the search box.

**RAG Pipeline Process:**
1. Query is embedded using `all-MiniLM-L6-v2` model
2. Semantic search in ChromaDB retrieves top 3 verses
3. Cosine similarity calculated between query and retrieved verses

**Top 3 Retrieved Results:**

| Rank | Verse | Similarity Score | Sanskrit Text (Kannada Script) |
|------|-------|------------------|--------------------------------|
| 1 | 20 | 0.8742 | ನ ಜಾಯತೇ ಮ್ರಿಯತೇ ವಾ ಕದಾಚಿನ್ನಾಯಂ ಭೂತ್ವಾ ಭವಿತಾ ವಾ ನ ಭೂಯಃ... |
| 2 | 23 | 0.8234 | ನೈನಂ ಛಿಂದಂತಿ ಶಸ್ತ್ರಾಣಿ ನೈನಂ ದಹತಿ ಪಾವಕಃ... |
| 3 | 24 | 0.7856 | ಅಚ್ಛೇದ್ಯೋಽಯಮದಾಹ್ಯೋಽಯಮಕ್ಲೇದ್ಯೋಽಶೋಷ್ಯ ಏವ ಚ... |

**Metrics Calculation:**
- **Answer Relevance:** cos_sim(query_embedding, verse_20_embedding) = 0.8742
- **Context Precision:** 3/3 verses above threshold (0.3) = 1.00

---

#### Query 2: "What is Karma Yoga?"

**Input:** User types "What is Karma Yoga?" in the search box.

**Top 3 Retrieved Results:**

| Rank | Verse | Similarity Score | Key Teaching |
|------|-------|------------------|--------------|
| 1 | 47 | 0.8521 | "Your right is to action alone, never to its results." |
| 2 | 48 | 0.8123 | "Perform action dwelling in Yoga, relinquishing attachment..." |
| 3 | 50 | 0.7945 | "Yoga is skill in action." |

**Metrics:**
- **Answer Relevance:** 0.8521
- **Context Precision:** 1.00

---

### B.5 Audio Output Examples

| Query | Language Selected | Audio Generated | Duration |
|-------|-------------------|-----------------|----------|
| What is the nature of the soul? | English | ✅ Yes | ~15 sec |
| ಆತ್ಮದ ಸ್ವರೂಪವೇನು? | Kannada | ✅ Yes | ~18 sec |
| What is Karma Yoga? | English | ✅ Yes | ~12 sec |

---

### B.6 Performance Metrics Summary

| Metric | Average Value | Description |
|--------|---------------|-------------|
| **Average Answer Relevance** | 0.82 | Cosine similarity between query and top result |
| **Average Context Precision** | 0.95 | Ratio of relevant results above threshold |
| **Query Response Time** | ~1.2 sec | Including embedding generation and retrieval |
| **TTS Generation Time** | ~2.5 sec | Audio generation for translation |
| **Relevance Threshold** | 0.30 | Minimum score to consider result relevant |

---

### B.7 Observations

1. **High Relevance Queries:** Spiritual and philosophical queries related to soul, duty, peace, and self-control show high relevance scores (0.75-0.90).

2. **Multilingual Support:** The system successfully handles both English and Kannada queries with comparable accuracy.

3. **Anti-Hallucination:** Queries unrelated to Bhagavad Gita content (e.g., general knowledge questions) are correctly identified and rejected with low relevance scores.

4. **Semantic Understanding:** The embedding model captures semantic meaning rather than keyword matching, enabling effective retrieval for paraphrased questions.

---

*Document Version: 1.0 | Generated: January 2026*
