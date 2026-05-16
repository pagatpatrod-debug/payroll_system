from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.basic_salary and self.employee:
            self.basic_salary = self.employee.basic_salary
        self.net_salary = self.basic_salary + self.allowances - self.deductions
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payroll for {self.employee} ({self.payroll_date})"
    
