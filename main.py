print("\n===== AI Resume Analyzer =====")

def load_keywords():
    with open("keywords.txt", "r") as f:
        return [line.strip().lower() for line in f]

def load_resume():
    filename = input("Enter resume file name (e.g., sample_resume.txt): ")

    try:
        with open(filename, "r") as f:
            return f.read().lower()
    except FileNotFoundError:
        print("❌ File not found!")
        return ""

def analyze_resume():
    keywords = load_keywords()
    resume = load_resume()

    if not resume:
        return

    found = []
    missing = []

    for word in keywords:
        if word in resume:
            found.append(word)
        else:
            missing.append(word)

    print("\n===== AI Resume Analyzer =====")

    print("\n Skills Found:")
    for f in found:
        print("-", f)

    print("\n Missing Skills:")
    for m in missing:
        print("-", m)

    print("\n Suggestions:")

    if "python" not in resume:
        print("- Add Python projects")
    if "sql" not in resume:
        print("- Add SQL knowledge")
    if "machine learning" not in resume:
        print("- Learn basics of Machine Learning")
    if "communication" not in resume:
        print("- Improve communication skills")

    
    total = len(keywords)
    score = (len(found) / total) * 100

    print(f"\n Resume Score: {score:.2f}%")

    if score < 40:
        print(" Needs major improvement")
    elif score < 70:
        print(" Can be improved")
    else:
        print(" Good resume")

    found = []
    missing = []

    for word in keywords:
        if word.lower() in resume.lower():
            found.append(word)
        else:
            missing.append(word)

    print("\n=== AI Resume Analyzer ===")

    print("\n Skills Found:")
    for f in found:
        print("-", f)

    print("\n Missing Skills:")
    for m in missing:
        print("-", m)

    print("\n Suggestions:")

    if "python" not in resume:
        print("- Add Python projects")
    if "sql" not in resume:
        print("- Add SQL knowledge")
    if "machine learning" not in resume:
        print("- Learn basics of Machine Learning")
    if "communication" not in resume:
        print("- Improve communication skills section")

analyze_resume()

