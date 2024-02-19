import pytest
from main import StudMlops
	def test_enroll():
		enr = StudMlops()
		enr.enroll(5)
		assert enr.totals() == 5
	def test_drop():
		dro = StudMlops()
		dro.enroll(10)
		dro.drop(3)
		assert dro.totals() == 12
	def test_getclass():
		names=StudMlops()
		assert names.getclass() == "mlops"
