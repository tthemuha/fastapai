from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_get_nonexistent_student():
    response = client.get("/api/student/nonexistent_student")
    assert response.status_code == 404
    assert "detail" in response.json()

def test_get_nonexistent_school():
    response = client.get("/api/school/nonexistent_school")
    assert response.status_code == 404
    assert "detail" in response.json()

def test_get_students_by_school():
    response = client.get("/api/student?school=IT School")
    assert response.status_code == 200
    data = response.json()["data"]
    assert isinstance(data, list)
    for student in data:
        assert student["school"] == "IT School"

def test_get_school_rooms_count():
    response = client.get("/api/school/IT School/rooms/count")
    assert response.status_code == 200
    assert "count" in response.json()
    assert isinstance(response.json()["count"], int)

def test_get_student_details():
    response = client.get("/api/student/Muhammadqodir/details")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "age" in data
    assert "school" in data

def test_get_school_teachers_count():
    response = client.get("/api/school/IT School/teachers/count")

    assert response.status_code == 200
    assert "count" in response.json()
    assert isinstance(response.json()["count"], int)

