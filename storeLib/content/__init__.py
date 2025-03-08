#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
class Content:
	def __init__(self, text=None, images=None, captions=None):
		self.text = text or ''
		self.images = images or []
		self.captions = captions or []
