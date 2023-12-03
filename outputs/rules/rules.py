def findDecision(obj): #obj[0]: Age, obj[1]: Gender, obj[2]: Polyuria, obj[3]: Polydipsia, obj[4]: sudden weight loss, obj[5]: weakness, obj[6]: Polyphagia, obj[7]: Genital thrush, obj[8]: visual blurring, obj[9]: Itching, obj[10]: Irritability, obj[11]: delayed healing, obj[12]: partial paresis, obj[13]: muscle stiffness, obj[14]: Alopecia, obj[15]: Obesity
	# {"feature": "Polyuria", "instances": 416, "metric_value": 0.2697, "depth": 1}
	if obj[2] == 'No':
		# {"feature": "Gender", "instances": 209, "metric_value": 0.3234, "depth": 2}
		if obj[1] == 'Male':
			# {"feature": "Polydipsia", "instances": 159, "metric_value": 0.1871, "depth": 3}
			if obj[3] == 'No':
				# {"feature": "Irritability", "instances": 132, "metric_value": 0.1192, "depth": 4}
				if obj[10] == 'No':
					# {"feature": "Alopecia", "instances": 119, "metric_value": 0.0767, "depth": 5}
					if obj[14] == 'No':
						return 'Negative'
					elif obj[14] == 'Yes':
						# {"feature": "Age", "instances": 57, "metric_value": 0.0676, "depth": 6}
						if obj[0]>37:
							# {"feature": "Itching", "instances": 54, "metric_value": 0.0606, "depth": 7}
							if obj[9] == 'Yes':
								return 'Negative'
							elif obj[9] == 'No':
								# {"feature": "visual blurring", "instances": 11, "metric_value": 0.0, "depth": 8}
								if obj[8] == 'No':
									return 'Negative'
								elif obj[8] == 'Yes':
									return 'Positive'
								else: return 'Positive'
							else: return 'Negative'
						elif obj[0]<=37:
							return 'Positive'
						else: return 'Positive'
					else: return 'Negative'
				elif obj[10] == 'Yes':
					# {"feature": "Genital thrush", "instances": 13, "metric_value": 0.2462, "depth": 5}
					if obj[7] == 'No':
						# {"feature": "Age", "instances": 10, "metric_value": 0.1333, "depth": 6}
						if obj[0]>42:
							return 'Negative'
						elif obj[0]<=42:
							# {"feature": "Polyphagia", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[6] == 'Yes':
								return 'Positive'
							elif obj[6] == 'No':
								return 'Negative'
							else: return 'Negative'
						else: return 'Positive'
					elif obj[7] == 'Yes':
						return 'Positive'
					else: return 'Positive'
				else: return 'Negative'
			elif obj[3] == 'Yes':
				# {"feature": "muscle stiffness", "instances": 27, "metric_value": 0.2852, "depth": 4}
				if obj[13] == 'No':
					# {"feature": "partial paresis", "instances": 15, "metric_value": 0.1, "depth": 5}
					if obj[12] == 'No':
						return 'Positive'
					elif obj[12] == 'Yes':
						# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 6}
						if obj[0]>49:
							return 'Positive'
						elif obj[0]<=49:
							return 'Negative'
						else: return 'Negative'
					else: return 'Positive'
				elif obj[13] == 'Yes':
					# {"feature": "delayed healing", "instances": 12, "metric_value": 0.1389, "depth": 5}
					if obj[11] == 'No':
						return 'Negative'
					elif obj[11] == 'Yes':
						# {"feature": "Irritability", "instances": 6, "metric_value": 0.1667, "depth": 6}
						if obj[10] == 'Yes':
							return 'Positive'
						elif obj[10] == 'No':
							# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[0]<=40:
								return 'Positive'
							elif obj[0]>40:
								return 'Negative'
							else: return 'Negative'
						else: return 'Positive'
					else: return 'Positive'
				else: return 'Negative'
			else: return 'Positive'
		elif obj[1] == 'Female':
			# {"feature": "Alopecia", "instances": 50, "metric_value": 0.2637, "depth": 3}
			if obj[14] == 'No':
				# {"feature": "Age", "instances": 38, "metric_value": 0.1561, "depth": 4}
				if obj[0]>34:
					# {"feature": "Irritability", "instances": 30, "metric_value": 0.0556, "depth": 5}
					if obj[10] == 'No':
						return 'Positive'
					elif obj[10] == 'Yes':
						# {"feature": "Polydipsia", "instances": 6, "metric_value": 0.0, "depth": 6}
						if obj[3] == 'Yes':
							return 'Positive'
						elif obj[3] == 'No':
							return 'Negative'
						else: return 'Negative'
					else: return 'Positive'
				elif obj[0]<=34:
					# {"feature": "visual blurring", "instances": 8, "metric_value": 0.0, "depth": 5}
					if obj[8] == 'No':
						return 'Negative'
					elif obj[8] == 'Yes':
						return 'Positive'
					else: return 'Positive'
				else: return 'Negative'
			elif obj[14] == 'Yes':
				# {"feature": "delayed healing", "instances": 12, "metric_value": 0.0, "depth": 4}
				if obj[11] == 'Yes':
					return 'Negative'
				elif obj[11] == 'No':
					return 'Positive'
				else: return 'Positive'
			else: return 'Negative'
		else: return 'Positive'
	elif obj[2] == 'Yes':
		# {"feature": "Polydipsia", "instances": 207, "metric_value": 0.0892, "depth": 2}
		if obj[3] == 'Yes':
			return 'Positive'
		elif obj[3] == 'No':
			# {"feature": "Itching", "instances": 52, "metric_value": 0.2637, "depth": 3}
			if obj[9] == 'Yes':
				# {"feature": "Genital thrush", "instances": 28, "metric_value": 0.2429, "depth": 4}
				if obj[7] == 'Yes':
					# {"feature": "Obesity", "instances": 18, "metric_value": 0.1905, "depth": 5}
					if obj[15] == 'No':
						return 'Positive'
					elif obj[15] == 'Yes':
						# {"feature": "sudden weight loss", "instances": 7, "metric_value": 0.0, "depth": 6}
						if obj[4] == 'No':
							return 'Positive'
						elif obj[4] == 'Yes':
							return 'Negative'
						else: return 'Negative'
					else: return 'Positive'
				elif obj[7] == 'No':
					# {"feature": "Age", "instances": 10, "metric_value": 0.0, "depth": 5}
					if obj[0]>41:
						return 'Negative'
					elif obj[0]<=41:
						return 'Positive'
					else: return 'Positive'
				else: return 'Negative'
			elif obj[9] == 'No':
				return 'Positive'
			else: return 'Positive'
		else: return 'Positive'
	else: return 'Positive'
