# 📄 GitHub Actions PDF CV Generator

This project allows you to dynamically generate a **beautiful, personalized PDF CV** using just a GitHub Action and a few text inputs.  
No manual formatting. No LaTeX. Just clean, automated resume generation with Python + ReportLab.

---

## 🚀 Features

- 🖋️ Fully formatted PDF with clean sections (Summary, Education, Experience, Projects, Skills)
- 📸 Optional profile image
- 🐙 GitHub and 🔗 LinkedIn icons in header
- 🛠️ Custom bullet summaries for each section
- 📤 Outputs a downloadable artifact via GitHub Actions

---

---

## ⚙️ How to Use It

1. **Fork or clone this repo**

2. Go to your **repo's "Actions" tab**  
   > 🟢 Enable GitHub Actions if prompted

3. Select **"Generate PDF CV"** workflow → Click **"Run workflow"**

4. Fill in the required fields:

   - 🧑 Name, email, phone
   - 📝 Summary (1–2 lines)
   - 🎓 Education: `Title::Description || Title::Description`
   - 💼 Experience: same format
   - 🚀 Projects: same format
   - 💡 Skills: comma-separated list
   - (Optional) GitHub & LinkedIn URLs
   - (Optional) Custom output filename

5. ✅ Wait for the workflow to finish

6. 📎 Download the PDF from the **Artifacts** section

---

## ❤️ Contributions
Feel free to fork and extend! Ideas for future improvements:

LaTeX/HTML export options

Drag-and-drop web UI

Multi-column CV layout
---





