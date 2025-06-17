import os

# ✅ Base setup
base_dir = os.path.join("Anna University", "R2021")
source_dept = "16. Computer Science and Engineering"
source_semester = os.path.join(base_dir, source_dept, "Semester 1")

# ✅ Ensure source exists
if not os.path.exists(source_semester):
    print("❌ Source Semester 1 not found!")
    exit()

# 🔁 Go through all departments
for dept_folder in os.listdir(base_dir):
    dept_path = os.path.join(base_dir, dept_folder)

    # ✅ Skip if not a folder or source itself
    if not os.path.isdir(dept_path) or dept_folder == source_dept:
        continue

    # 🎯 Destination link path
    link_path = os.path.join(dept_path, "Semester 1")

    # 🧪 Check if link/folder already exists
    if os.path.exists(link_path):
        print(f"⚠️ Skipping {dept_folder}: 'Semester 1' already exists.")
        continue

    # 📌 Create relative path from current department to source semester
    rel_path = os.path.relpath(source_semester, dept_path)

    try:
        os.symlink(rel_path, link_path)
        print(f"🔗 Linked: {dept_folder}/Semester 1 ➝ {rel_path}")
    except Exception as e:
        print(f"❌ Failed to link in {dept_folder}: {e}")
