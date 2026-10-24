cat > classification.py << 'EOF'
def classify(value, threshold=0.5):
"""Simple threshold classifier."""
return 1 if value >= threshold else 0

