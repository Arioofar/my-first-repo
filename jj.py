import arcpy


def get_nomber(infc):
    return (len(arcpy.ListFields(infc)))