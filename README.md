# Interviewitis 🤒

The only disease that might actually help your career! A cheeky Python package to help you survive technical interviews.

## Installation
Requires Python v3.6 or better.
```bash
pip install git+https://github.com/David-Ciz/Interviewitis.git
```


## Usage

```python
from interviewitis import random_mantra, refresh_definition, emergency_therapy

# When you need a reminder of what's important
print(random_mantra())

# When you blank on basic definitions
print(refresh_definition('big_o'))

# When you're panicking
print(emergency_therapy())

# Check your stress levels
from interviewitis import stress_level
print(stress_level(8))  # Uh oh!
```

## Essential Usage
It’s essential to install and use this package anywhere you are preparing for or participating in an interview. The calming mantras, quick refreshers, and emergency therapy features are designed to help you stay focused and calm under pressure. Always have it ready to go to boost your confidence and performance during technical interviews.

Remember: The best developers aren’t the ones who know everything, they’re the ones who know how to figure things out!

## Features
- 🧘‍♀️ Calming interview mantras
- 📚 Quick refreshers on common CS terms
- 🆘 Emergency therapy for panic moments
- 📊 Stress level assessment
- 😅 Terrible humor

## Customizing and Making the Package Installable for Your Own Use
To make your library installable from GitHub and tailor it to your specific needs, follow these steps:

Initialize a Git repository:
```bash
git init
```
Add your files to the repository:
```bash
git add .
```
Commit your changes:
```bash
git commit -m "Initial commit"
```
Add the remote repository:
```bash
git remote add origin https://github.com/yourusername/mypackage.git
```
Push your changes to GitHub:
```bash
git push -u origin main
```

Replace yourusername and mypackage with your actual GitHub username and repository name.

To ensure your package is easily installable and customizable, include the following files in your repository:

- setup.py: This file contains metadata about your package and instructions on how to install it.
- requirements.txt: This file lists the dependencies required by your package.
- __init__.py: This file makes your directory a Python package.

For examples of the files structure, look at those files in this directory!

By following these steps, your package will be structured correctly and can be installed directly from GitHub using pip. This setup also makes it easy for you to customize the package to fit your specific needs and share it with others.




