from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Course


class CourseModelTests(TestCase):
	def test_course_creation(self):
		course=Course.objects.create(
			title="Python Regular Expressions",
			description="Learn to write regular expressions in python"
		)
		now=timezone.now()
		self.assertLess(course.created_at, now)



class CourseViewsTests(TestCase):
	def setUp(self):
		self.course = Course.objects.create(
			title="Python Testing",
			description="Learn to write tests in Python"
		)
		self.course2 = Course.objects.create(
			title="New Course",
			description="A new course"
		)
		self.step=Step.objects.create(
			title="Introduction to Doctests",
			course=self.course
		)

		def test_course_list_view(self):
			resp = self.client.get(reverse('courses:course_list'))
			self.assertEqual(resp.status_code, 200)
			self.assertIn(self.course, resp.context['courses'])
			self.assertIn(self.course2, resp.context['courses'])
			self.assertTemplateUsed(resp, 'courses/course_list.html')
			self.assertContains(resp, self.course.title)

		def test_course_detail_view(self):
			resp = self.client.get(reverse('courses:course_detail', kwargs={'pk':self.course.pk}))
			self.assertEqual(resp.status_code, 200)
			self.assertEqual(self.course, resp.context['course'])

		def test_step_detail_view(self):
			resp = self.client.get(reverse('courses:course_detail', kwargs={'pk':self.course.pk, 'step_pk':self.step.pk}))	
			self.assertEqual(resp.status_code, 200)
			self.assertEqual(self.step, resp.context['step'])
