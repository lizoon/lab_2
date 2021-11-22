<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<body>
				<table border = "2" width = "80%" height = "90%" bgcolor = "#FAE6E8" bordercolor = "#E0BFA6">
					<tr>
						<th rowspan = "3">Name</th>
						<th rowspan = "3">Surname</th>
						<th rowspan = "3">Patronym</th>
						<th rowspan = "3">Faculty</th>
						<th rowspan = "3">Department</th>
						<th rowspan = "3">Education</th>
						<th rowspan = "3">Place of education</th>
						<th>Day of beginning of education</th>
						<th>Day of ending of education</th>
					</tr>
					<tr>
						<th>Month of beginning of education</th>
						<th>Month of ending of education</th>
					</tr>
					<tr>
						<th>Year of beginning of education</th>
						<th>Year of ending of education</th>
					</tr>
					<xsl:for-each select = "educationDataBase/person">
						<tr>
							<td rowspan = "3" align = "center"><xsl:value-of select="name"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="surname"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="patronym"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="faculty"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="department"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="education"/></td>
							<td rowspan = "3" align = "center"><xsl:value-of select="place_educ"/></td>
							<xsl:for-each select = "date_begin">
								<td align = "center"><xsl:value-of select="number"/></td></xsl:for-each>
							<xsl:for-each select = "date_end">
									<td align = "center"><xsl:value-of select="number"/></td></xsl:for-each>
							<tr>
							<xsl:for-each select = "date_begin">
								<td align = "center"><xsl:value-of select="month"/></td></xsl:for-each>
							<xsl:for-each select = "date_end">
									<td align = "center"><xsl:value-of select="month"/></td></xsl:for-each>
							</tr>
							<tr>
							<xsl:for-each select = "date_begin">
								<td align = "center"><xsl:value-of select="year"/></td></xsl:for-each>
							<xsl:for-each select = "date_end">
								<td align = "center"><xsl:value-of select="year"/></td></xsl:for-each>
							</tr>
						</tr>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
