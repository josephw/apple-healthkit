<?xml version="1.0"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/HealthData">
    <HealthData>
      <xsl:apply-templates select="Workout[@workoutActivityType='HKWorkoutActivityTypeSwimming']"/>
    </HealthData>
  </xsl:template>
  <xsl:template match="Workout">
    <xsl:copy-of select="."/>
  </xsl:template>
</xsl:stylesheet>
