import mysql.connector
def insert_subtasks():
    conn = mysql.connector.connect(
    host="10.95.136.128",
    user="app_user", 
    password="Mohammed&meeraj786", 
    database="timesheet",
)
    cursor = conn.cursor()

    project_id=86
    project_name = "6m tall sliding"
    pspelement = "6m tall sliding"
    created_by = "Ashwini"
    subtasks = [
    "D1 - Spec Sheet (What is possible, what is not possible? - First Idea)",
    "D1 - Prestudy",
    "D1 - Technical effort estimation (number of new profiles, drawings...etc)",
    "D1 - Analyzing current market trends",
    "D1 - Searching and finalizing the potential supplier (Vendor)",
    "D1 - Project budget creation",
    "D1 - Project Plan creation",
    "D1 - Concept Study",
    "D1 - D1 Signoff",
    "D2 - Detailed Concept R&D",
    "D2 - Plan to Schucal documents",
    "D2 - Prototyping",
    "D2 - Element costing",
    "D2 - Concept Freeze",
    "D3 - Material Creation SAP - Y1 (Material Pre-Planning)",
    "D3 - Master article list creation",
    "D3 - Finalizing and creation of article models + drawings + ACAD Symbols",
    "D3 - Review and Update of drawings",
    "D3 - Master model Creation for Documentation",
    "D3 - DMU Review & Update",
    "D3 - Advanced test planning + information to Test Institute",
    "D3 - Catalogues planning",
    "D3 - FSR release",
    "D3 - Test Element Drawings creation",
    "D3 - Element costing/Pricing update",
    "D3 - Master article freeze",
    "D3 - PDM Data Maintenance",
    "D4 - Testing & Documentation",
    "D4 - Order manual preparation and handover first draft",
    "D4 - Fabrication assembly and installation manuals review and final drafts",
    "D4 - FSR Approval (Ready for Order)",
    "D4 - Test Report Review and approval",
    "D5 - Test certificates upload",
    "D5 - Product training",
    "D5 - Marketing strategy"
]


    values = [(project_id,project_name, pspelement, subtask, created_by) for subtask in subtasks]

    query = """
    INSERT INTO subtasks (project_id,project_name, pspelement, subtask, created_by)
    VALUES (%s, %s, %s, %s,%s)
    """





    try:
        cursor.executemany(query, values)
        conn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")
    except mysql.connector.Error as err:
        print("Error occurred while inserting:", err)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    insert_subtasks()