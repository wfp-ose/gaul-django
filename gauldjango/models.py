from django.contrib.gis.db import models

class GAULAdmin0(models.Model):
    """
    GAUL Admin 0
    """
    id = models.AutoField(primary_key=True,  db_index=True)
    admin0_code = models.IntegerField(null=True, db_index=True)
    admin0_name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    disp_area = models.CharField(max_length=255, null=True, blank=True)
    mpoly = models.MultiPolygonField('Multi-polygon', srid=4326, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return "%s" % self.admin0_name.encode('utf-8')

    class Meta:
        ordering = ("admin0_code",)
        verbose_name = 'GAUL, Admin 0 District'
        verbose_name_plural = 'GAUL, Admin 0 District'

class GAULAdmin1(models.Model):
    """
    GAUL Admin 1
    """
    id = models.AutoField(primary_key=True, db_index=True)
    admin0 = models.ForeignKey(GAULAdmin0, db_index=True, null=True)
    admin1_code = models.IntegerField(db_index=True, null=True)
    admin1_name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    disp_area = models.CharField(max_length=255, null=True, blank=True)
    mpoly = models.MultiPolygonField('Multi-polygon', srid=4326, null=True)
    objects = models.GeoManager()

    @property
    def admin0_code(self):
        if self.admin0_id:
            return GAULAdmin0.objects.filter(pk=self.admin0_id).values_list('admin0_code', flat=True)[0]
        else:
            return None

    @property
    def admin0_name(self):
        if self.admin0_id:
            return GAULAdmin0.objects.filter(pk=self.admin0_id).values_list('admin0_name', flat=True)[0]
        else:
            return None

    def __str__(self):
        return "%s, %s" % self.admin0_name.encode('utf-8'), self.admin1_name.encode('utf-8')

    class Meta:
        ordering = ("admin0__admin0_code", "admin1_code",)
        verbose_name = 'GAUL, Admin 1 Districts'
        verbose_name_plural = 'GAUL, Admin 1 Districts'

class GAULAdmin2(models.Model):
    """
    GAUL Admin 2
    """
    id = models.AutoField(primary_key=True, db_index=True)
    admin1 = models.ForeignKey(GAULAdmin1, db_index=True, null=True)
    admin2_code = models.IntegerField(db_index=True, null=True)
    admin2_name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    disp_area = models.CharField(max_length=255, null=True, blank=True)
    mpoly = models.MultiPolygonField('Multi-polygon', srid=4326, null=True)
    objects = models.GeoManager()

    @property
    def admin0_code(self):
        if self.admin1_id:
            return GAULAdmin1.objects.filter(pk=self.admin1_id).values_list('admin0__admin0_code', flat=True)[0]
        else:
            return None

    @property
    def admin0_name(self):
        if self.admin1_id:
            return GAULAdmin1.objects.filter(pk=self.admin1_id).values_list('admin0__admin0_name', flat=True)[0]
        else:
            return None

    @property
    def admin1_code(self):
        if self.admin1_id:
            return GAULAdmin1.objects.filter(pk=self.admin1_id).values_list('admin1_code', flat=True)[0]
        else:
            return None

    @property
    def admin1_name(self):
        if self.admin1_id:
            return GAULAdmin1.objects.filter(pk=self.admin1_id).values_list('admin1_name', flat=True)[0]
        else:
            return None

    def __str__(self):
        return "%s, %s, %s" % self.admin0_name.encode('utf-8'), self.admin1_name.encode('utf-8'), self.admin2_name.encode('utf-8')

    class Meta:
        ordering = ("admin1__admin0__admin0_code", "admin1__admin1_code", "admin2_code",)
        verbose_name = 'GAUL, Admin 2 District'
        verbose_name_plural = 'GAUL, Admin 2 District'
