# Task 3: CBOW vs Skip-Gram

## CBOW

Context → Target Word

Example:

"I love ____ learning"

Predict:
machine

Advantages:
- Faster training
- Works well on large datasets

Use When:
- Dataset is large
- Speed is important

---

## Skip-Gram

Target Word → Context Words

Example:

machine

Predict:
love, learning

Advantages:
- Better for rare words
- Better semantic understanding

Use When:
- Dataset is small
- Rare words matter