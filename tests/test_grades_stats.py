from services.university.models.grade_request import GradeRequest


class TestGradesStats:

    def _create_test_grade(self, university_service_admin, student_id: int, teacher_id: int, grade: int):
        grade_request = GradeRequest(
            teacher_id=teacher_id,
            student_id=student_id,
            grade=grade
        )
        return university_service_admin.create_grade(grade_request)

    def test_stats_returns_200_without_params(self, university_service_admin):
        stats = university_service_admin.get_grades_stats()
        assert stats.count >= 0, f"Ожидался count >= 0, получен {stats.count}"

    def test_stats_returns_200_with_student_id(self, university_service_admin, test_student):
        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.count == 0, f"Ожидался count = 0, получен {stats.count}"

    def test_stats_returns_200_with_teacher_id(self, university_service_admin, test_teacher):
        stats = university_service_admin.get_grades_stats(teacher_id=test_teacher)
        assert stats.count == 0, f"Ожидался count = 0, получен {stats.count}"

    def test_stats_returns_200_with_group_id(self, university_service_admin, test_group):
        stats = university_service_admin.get_grades_stats(group_id=test_group)
        assert stats.count == 0, f"Ожидался count = 0, получен {stats.count}"

    def test_stats_returns_403_without_token(self, university_service_anonym):
        response = university_service_anonym.grades_helper.get_stats()
        assert response.status_code == 403, \
            f"Ожидался статус 403, получен {response.status_code}"

    def test_stats_min_is_none_when_no_data(self, university_service_admin, test_student):
        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.min is None, f"Ожидался min = None, получен {stats.min}"

    def test_stats_max_is_none_when_no_data(self, university_service_admin, test_student):
        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.max is None, f"Ожидался max = None, получен {stats.max}"

    def test_stats_avg_is_none_when_no_data(self, university_service_admin, test_student):
        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.avg is None, f"Ожидался avg = None, получен {stats.avg}"

    def test_stats_min_calculated_correctly(self, university_service_admin, test_student, test_teacher):
        self._create_test_grade(university_service_admin, test_student, test_teacher, 2)
        self._create_test_grade(university_service_admin, test_student, test_teacher, 5)

        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.min == 2, f"Ожидался min = 2, получен {stats.min}"

    def test_stats_max_calculated_correctly(self, university_service_admin, test_student, test_teacher):
        self._create_test_grade(university_service_admin, test_student, test_teacher, 2)
        self._create_test_grade(university_service_admin, test_student, test_teacher, 5)

        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.max == 5, f"Ожидался max = 5, получен {stats.max}"

    def test_stats_avg_calculated_correctly(self, university_service_admin, test_student, test_teacher):
        self._create_test_grade(university_service_admin, test_student, test_teacher, 2)
        self._create_test_grade(university_service_admin, test_student, test_teacher, 5)

        stats = university_service_admin.get_grades_stats(student_id=test_student)
        assert stats.avg == 3.5, f"Ожидался avg = 3.5, получен {stats.avg}"

    def test_filter_by_student_id_returns_correct_count(self, university_service_admin, student_a_with_grades, student_b_with_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_a_with_grades)
        assert stats.count == 2, f"Ожидался count = 2, получен {stats.count}"

    def test_filter_by_student_id_returns_correct_min(self, university_service_admin, student_a_with_grades, student_b_with_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_a_with_grades)
        assert stats.min == 4, f"Ожидался min = 4, получен {stats.min}"

    def test_filter_by_student_id_returns_correct_max(self, university_service_admin, student_a_with_grades, student_b_with_grades):
        stats = university_service_admin.get_grades_stats(student_id=student_a_with_grades)
        assert stats.max == 5, f"Ожидался max = 5, получен {stats.max}"

    def test_filter_by_teacher_id_returns_correct_count(self, university_service_admin, teacher_x_with_grades,
                                                        teacher_y_with_grades):
        stats = university_service_admin.get_grades_stats(teacher_id=teacher_x_with_grades)
        assert stats.count == 3, f"Ожидался count = 3, получен {stats.get('count')}"

    def test_filter_by_teacher_id_returns_correct_min(self, university_service_admin, teacher_x_with_grades,
                                                      teacher_y_with_grades):
        stats = university_service_admin.get_grades_stats(teacher_id=teacher_x_with_grades)
        assert stats.min == 4, f"Ожидался min = 4, получен {stats.get('min')}"

    def test_filter_by_teacher_id_returns_correct_max(self, university_service_admin, teacher_x_with_grades,
                                                      teacher_y_with_grades):
        stats = university_service_admin.get_grades_stats(teacher_id=teacher_x_with_grades)
        assert stats.max == 5, f"Ожидался max = 5, получен {stats.get('max')}"

    def test_filter_by_group_id_returns_correct_count(self, university_service_admin, group1_with_grades,
                                                      group2_with_grades):
        stats = university_service_admin.get_grades_stats(group_id=group1_with_grades)
        assert stats.count == 3, f"Ожидался count = 3, получен {stats.get('count')}"

    def test_filter_by_group_id_returns_correct_min(self, university_service_admin, group1_with_grades,
                                                    group2_with_grades):
        stats = university_service_admin.get_grades_stats(group_id=group1_with_grades)
        assert stats.min == 3, f"Ожидался min = 3, получен {stats.get('min')}"

    def test_filter_by_group_id_returns_correct_max(self, university_service_admin, group1_with_grades,
                                                    group2_with_grades):
        stats = university_service_admin.get_grades_stats(group_id=group1_with_grades)
        assert stats.max == 5, f"Ожидался max = 5, получен {stats.get('max')}"

    def test_filter_by_student_and_teacher_returns_correct_count(self, university_service_admin,
                                                                 student_a_teacher_x_with_grade):
        student_a, teacher_x = student_a_teacher_x_with_grade
        stats = university_service_admin.get_grades_stats(student_id=student_a, teacher_id=teacher_x)
        assert stats.count == 1, f"Ожидался count = 1, получен {stats.get('count')}"

    def test_filter_by_student_and_teacher_returns_correct_min(self, university_service_admin,
                                                               student_a_teacher_x_with_grade):
        student_a, teacher_x = student_a_teacher_x_with_grade
        stats = university_service_admin.get_grades_stats(student_id=student_a, teacher_id=teacher_x)
        assert stats.min == 5, f"Ожидался min = 5, получен {stats.get('min')}"

    def test_filter_by_student_and_teacher_returns_correct_max(self, university_service_admin,
                                                               student_a_teacher_x_with_grade):
        student_a, teacher_x = student_a_teacher_x_with_grade
        stats = university_service_admin.get_grades_stats(student_id=student_a, teacher_id=teacher_x)
        assert stats.max == 5, f"Ожидался max = 5, получен {stats.get('max')}"

    def test_nonexistent_student_returns_count_zero(self, university_service_admin, max_student_id):
        nonexistent_id = max_student_id + 1
        stats = university_service_admin.get_grades_stats(student_id=nonexistent_id)
        assert stats.count == 0, f"Ожидался count = 0, получен {stats.get('count')}"

    def test_nonexistent_student_returns_min_none(self, university_service_admin, max_student_id):
        nonexistent_id = max_student_id + 1
        stats = university_service_admin.get_grades_stats(student_id=nonexistent_id)
        assert stats.min is None, f"Ожидался min = None, получен {stats.get('min')}"

    def test_nonexistent_student_returns_max_none(self, university_service_admin, max_student_id):
        nonexistent_id = max_student_id + 1
        stats = university_service_admin.get_grades_stats(student_id=nonexistent_id)
        assert stats.max is None, f"Ожидался max = None, получен {stats.get('max')}"

    def test_nonexistent_student_returns_avg_none(self, university_service_admin, max_student_id):
        nonexistent_id = max_student_id + 1
        stats = university_service_admin.get_grades_stats(student_id=nonexistent_id)
        assert stats.avg is None, f"Ожидался avg = None, получен {stats.get('avg')}"

    def test_stats_consistency(self, university_service_admin):
        stats1 = university_service_admin.get_grades_stats()
        stats2 = university_service_admin.get_grades_stats()
        assert stats1 == stats2, f"Статистика не совпадает:\n{stats1}\n{stats2}"
