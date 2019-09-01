from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=9, blank=True, null=True)
    dept_choice = (
        ('Computer science', 'Computer science'),
        ('Microbiology', 'Microbiology'),
        ('Biochemistry', 'Biochemistry'),
        ('Economics', 'Economics'),
        ('English', 'English'),
        ('Sociology', 'Sociology'),
    )
    department = models.CharField(choices=dept_choice, max_length=30, blank=True, null=True)
    Faculty_choice = (
        ('Faculty of Science', 'Faculty of Science'),
        ('Faculty of Arts and Social Management science', 'Faculty of Arts'),
        ('Faculty of Law', 'Faculty of law'),
        ('Faculty of Health Science', 'Faculty of Health'),
    )
    faculty = models.CharField(choices=Faculty_choice, max_length=100, blank=True, null=True)
    LEVEL = (
        ('100 level', '100 level'),
        ('200 level', '200 level'),
        ('300 level', '300 level'),
        ('400 level', '400 level'),
    )
    level = models.CharField(choices=LEVEL, max_length=20, blank=True, null=True)
    SEX = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    sex = models.CharField(choices=SEX, max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} StudentProfile'

    def save(self, *args, **kwargs):
        super().save()


# def create_profile(sender=User, **kwargs):
#
#     if kwargs['created']:
#         stud_profile = Profile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)



class Result(models.Model):
    student = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10, null=True, blank=True)
    course_title = models.CharField(max_length=200, null=True, blank=True)
    UNIT = [('6', '6'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')]
    course_unit = models.CharField(max_length=1, choices=UNIT)
    TYPE = [('C', 'C'), ('E', 'E')]
    course_type = models.CharField(max_length=1, choices=TYPE)
    total_score = models.PositiveIntegerField()
    GRADE_PT = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )
    grade_pt = models.CharField(max_length=1, default=5, choices=GRADE_PT)
    SESSION = [('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'),
               ('2019/2020', '2019/2020')]
    session = models.CharField(max_length=30, choices=SESSION)
    SEM = [('1st Semester', '1st Semester'), ('2nd Semester', '2nd Semester')]
    semester = models.CharField(max_length=30, choices=SEM)

    def __str__(self):
        return self.student.first_name + " " + self.course_code
