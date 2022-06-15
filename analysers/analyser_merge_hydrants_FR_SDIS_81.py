#!/usr/bin/env python
#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Lucas Longour 2022                                         ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from .analyser_merge_hydrants_FR import _Analyser_Merge_Afigeo_Hydrants
from .Analyser_Merge import Source


class Analyser_Merge_Hydrants_FR_SDIS_81(_Analyser_Merge_Afigeo_Hydrants):
    def __init__(self, config, logger = None):
        _Analyser_Merge_Afigeo_Hydrants.__init__(self, config,
            source_url='https://www.data.gouv.fr/fr/datasets/hydrants-du-tarn/',
            dataset_name='Points d\'eau incendie répertoriés dans le Tarn',
            source=Source(attribution='Service départemental d\'incendie et de secours 81',
                millesime='2021-04',
                fileUrl='https://deci.sdis81.fr/geoserver/sdis81/ows?service=WFS&request=GetFeature&srsName=EPSG:4326&typename=sdis81:pei_81_mm&outputFormat=application/json'),
            osmRef='ref:FR:SDIS81',
            logger=logger)
