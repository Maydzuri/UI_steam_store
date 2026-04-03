from services.university.models.grades_stats_response import GradesStatsResponse


class TestGradesStats:

    def test_stats_returns_200_without_params(self, university_service_admin):
        response = university_service_admin.grades_helper.get_stats()
        assert response.status_code == 200

    def test_stats_returns_200_with_student_id(self, university_service_admin):
        response = university_service_admin.grades_helper.get_stats(student_id=1)
        assert response.status_code == 200

    def test_stats_returns_200_with_teacher_id(self, university_service_admin):
        response = university_service_admin.grades_helper.get_stats(teacher_id=1)
        assert response.status_code == 200

    def test_stats_returns_200_with_group_id(self, university_service_admin):
        response = university_service_admin.grades_helper.get_stats(group_id=1)
        assert response.status_code == 200

    def test_stats_returns_401_without_token(self, university_service_anonym):
        response = university_service_anonym.grades_helper.get_stats()
        assert response.status_code == 401, \
            f"Ожидался статус 401, получен {response.status_code}"

    def test_stats_service_returns_valid_model(self, university_service_admin):
        stats = university_service_admin.get_grades_stats()
        assert isinstance(stats, GradesStatsResponse)
        assert stats.count >= 0

        if stats.count > 0:
            assert stats.min >= 0
            assert stats.max >= 0
            assert stats.avg >= 0
        else:
            assert stats.min is None
            assert stats.max is None
            assert stats.avg is None

    def test_stats_business_logic(self, university_service_admin):
        stats = university_service_admin.get_grades_stats()
        if stats.count > 0:
            assert stats.min is not None
            assert stats.max is not None
            assert stats.avg is not None
            assert stats.min <= stats.avg <= stats.max

    def test_stats_filter_by_student(self, university_service_admin):
        stats_all = university_service_admin.get_grades_stats()
        stats_for_student = university_service_admin.get_grades_stats(student_id=1)

        if stats_all.count > 0 and stats_for_student.count > 0:
            assert stats_for_student.count <= stats_all.count

    def test_stats_consistency(self, university_service_admin):
        stats1 = university_service_admin.get_grades_stats()
        stats2 = university_service_admin.get_grades_stats()
        assert stats1.count == stats2.count
        if stats1.count > 0:
            assert stats1.min == stats2.min
            assert stats1.max == stats2.max
            assert stats1.avg == stats2.avg
