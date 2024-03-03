from filexdb import FileXdb


# Create an instance of Database
db = FileXdb("test_DB", "test_data/db")

# Create a Collection
student_info = db.collection("student_info")
student_2 = db.collection("student_2")


def test_insert():
    assert student_info.insert({"name": "Sam", "roll": "CSE/17/19", "dept": "CSE"})
    assert student_info.insert({"name": "Bob", "roll": "EE/01/18", "dept": "EE", "skill": ["python", "c++"]})
    assert student_info.insert({"name": "Rana", "dept": "CSE"})
    assert student_2.insert({"name": "Rana", "dept": "CSE"})


def test_insert_all():
    assert student_info.insert_all([
        {"name": "Addy", "roll": "ME/57/19", "dept": "ME", "cgpa": 9.05},
        {"name": "Roman", "roll": "ECE/80/13", "dept": "ECE", "skill": ["game design"], "spc": ["Blinder"]},
        {"name": "Sam"}
    ])
    assert student_2.insert_all([
        {"name": "Addy", "roll": "CSE/57/19", "dept": "CSE", "cgpa": 9.05},
        {"name": "Roman", "roll": "CSE/80/13", "dept": "CSE", "skill": ["game design"], "spc": ["Blinder"]},
        {"name": "Sam", "dept": "CSE"}
    ])


def test_find():
    _query_1 = {"name": "Sam"}

    assert student_info.find()                                  # Returns all Documents.
    assert student_info.find(query=_query_1)                    # Returns all Documents matches the ``_query``.
    assert student_info.find(query=_query_1, limit=(1, 3))      # Returns doc[1] to doc[2] matches the ``_query``.
    assert student_info.find(limit=(1, 10))                     # Returns doc[1] to doc[9] of all Documents.

    # with multiple query
    _query_2 = {"name": "Sam", "roll": "CSE/17/19"}

    assert student_info.find()                                  # Returns all Documents.
    assert student_info.find(query=_query_2)                    # Returns all Documents matches the ``_query``.
    assert student_info.find(query=_query_2, limit=(0, 30))     # Returns doc[1] to doc[2] matches the ``_query``.
    assert student_info.find(limit=(1, 10))                     # Returns doc[1] to doc[9] of all Documents.


def test_count_item():
    _query_1 = {"name": "Sam"}

    assert student_info.find().count_item()
    assert student_info.find(query=_query_1).count_item()
    assert student_info.find(query=_query_1, limit=(1, 3)).count_item()
    assert student_info.find(limit=(1, 10)).count_item()


def test_export():
    _query_1 = {"name": "Sam"}

    student_info.find().export("test-db-Sam-1", "test_data/export")
    student_info.find(query=_query_1).export("test-db-Sam-2", "test_data/export")
    student_info.find(query=_query_1, limit=(1, 3)).export("test-db-Sam-3", "test_data/export")
    student_info.find(limit=(1, 10)).export("test-db-Sam-4", "test_data/export")


def test_delete():
    assert student_info.delete({"name": "Addy"})
    assert student_info.delete({"name": "Sam", "roll": "CSE/17/19"})
    assert student_info.delete({"name": "Roman", "roll": "ECE/80/13", "dept": "ECE"})


def test_update_document():
    assert student_info.update({"passed": True, "mobile": 123456789}, {"name": "Bob"})
    assert student_info.update({"name": "The Sam", "skill": ["C++", "Python"]}, {"name": "Sam"})
    assert student_info.update({"dept": "Computer Science & Engineering"}, {"dept": "CSE"})


def test_rename():
    student_2.rename("student_info_cse")


def test_drop():
    student_info.drop()


