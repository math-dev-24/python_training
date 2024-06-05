from typing import List, Dict, Any, Tuple

DATA_STUDENT: Tuple[Tuple[str, Tuple[float, ...]], ...] = (
    ('Tao', (18, 12, 3, 5, 19)),
    ('Josette', (20, 2, 12, 18, 14)),
    ('Patrick', (2, 4, 6, 18, 17)),
    ('Pema', (3, 19, 15, 3, 12)),
    ('Jean', (0, 9, 8, 8, 4)),
    ('Bixente', (14, 20, 10, 12, 4)),
    ('Paco', (16, 1, 1, 1, 20)),
    ('Chuluun', (15, 6, 17, 20, 15)),
    ('Marie', (16, 4, 16, 20, 12)),
    ('Mohamed', (16, 19, 17, 6, 20)),
)


def average_student_score(name: str, notes: Tuple[float, ...]) -> Dict[str, Any]:
    return {
        "name": name,
        "notes": notes,
        "average": round(sum(notes) / len(notes))
    }


def sort_students_by_average(students: List[Dict[str, Any]]) -> None:
    students_sorted_by_average = sorted(students, key=lambda item: item['average'], reverse=True)
    print(
        "".join(
            f"{rank:2d} : {student['name']} avec une moyenne de {student['average']}/20 \n"
            for rank, student in enumerate(students_sorted_by_average, start=1)
            )
    )


if __name__ == "__main__":
    classroom = [average_student_score(student[0], student[1]) for student in DATA_STUDENT]
    sort_students_by_average(classroom)
