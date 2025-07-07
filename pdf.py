from fpdf import FPDF

# Create PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# IEEE References
references = [
    "1. V. Savin, \"Build a Full-Stack Spotify Clone with React Native, Expo, and GraphQL,\" *notjust.dev*. [Online]. Available: https://www.notjust.dev/projects/spotify.",
    "2. R. Ranawat, \"Flutter Full-Stack Tutorial: Spotify Clone w/ MVVM Architecture, Python, FastAPI & Riverpod,\" *ceppek.com*, Nov. 14, 2024. [Online]. Available: https://ceppek.com/2024/11/14/flutter-full-stack-tutorial-spotify-clone-w-mvvm-architecture-python-fastapi-riverpod/.",
    "3. K. Angara, \"How to build a Spotify clone using React and ts-audio,\" *LogRocket Blog*, Jan. 12, 2023. [Online]. Available: https://blog.logrocket.com/build-spotify-clone-react-ts-audio/.",
    "4. P. Dwivedi, \"How to build Spotify clone in Android,\" *GeeksforGeeks*, Sep. 2, 2022. [Online]. Available: https://www.geeksforgeeks.org/how-to-build-spotify-clone-in-android/.",
    "5. R. Batey, \"Build your own Spotify clone using JavaScript, PHP and MySQL,\" *Udemy.com*, 2022. [Online]. Available: https://www.udemy.com/course/spotify-clone/.",
    "6. A. Deosthale, \"Spotify Clone using ReactJS - The Ultimate Guide,\" *Medium*, Jan. 14, 2021. [Online]. Available: https://medium.com/cleverprogrammer/spotify-clone-using-reactjs-the-ultimate-guide-2a47977a1e4f."
]

# Replace unsupported characters
def sanitize_text(text):
    return text.replace("–", "-").replace("’", "'").replace("“", '"').replace("”", '"')

# Add references to PDF
for ref in references:
    sanitized_ref = sanitize_text(ref)
    pdf.multi_cell(0, 10, sanitized_ref)
    pdf.ln(1)

# Save the PDF
pdf.output("Spotify_Clone_References_IEEE.pdf")