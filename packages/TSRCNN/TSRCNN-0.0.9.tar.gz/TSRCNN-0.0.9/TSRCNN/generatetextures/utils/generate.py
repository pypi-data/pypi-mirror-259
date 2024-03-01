import os	# 파이썬 기본 내제 모율, 운영체제와 상호작용을 돕는 다양한 기능 제공 (디렉토리 확인변경, csv 파일 호출 ..)
import numpy as np	# 벡터 및 행렬 연산
import cv2	# OpenCV import -> 오픈소스 컴퓨터 비전 및 머신러닝 라이브러리
			# 먼저 설치 : pip install opencv-python
from math import ceil	# math 함수 -> ceil : 올림 (int형)
import math	# 추가 : 사인 코사인 탄젠트 사용을 위해
from itertools import product	# itertools : 순열, 조합, product 구현,사용
				# poduct : 데카르트 곱 (cartesian product) = 2개 이상의 리스트의 모든 조합 구함

inf = float('inf')	# 그 자체로 ∞를 의미
ErrorCombinationFunc = np.add	# np.add: array 요소 단위로 덧셈 계산..

# original #########################
# original 사용 함수
def findPatchHorizontal(refBlock, texture, blocksize, overlap, tolerance):	# tolerance : 허용오차
	'''
	Find best horizontal match from the texture
	사용: findPatchHorizontal(refBlock, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성 / inf 는 왜더하는지는 모르겠음???
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# openCV 경우 -> (rows, columns, channels) 튜플 보유,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)
		rmsVal = ((texture[i:i+blocksize, j:j+overlap] - refBlock[:, -overlap:])**2).mean()	# (이웃 블록의 오버랩 부분 - 각 블록의 오버랩 부분) 제곱 의 평균
		if rmsVal > 0:
			errMat[i, j] = rmsVal	# 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것
	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E 고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기
	c = np.random.randint(len(y))	# random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
	y, x = y[c], x[c]	# 허용오차 안의 해당 에러 중 랜덤하게 뽑음

	return texture[y:y+blocksize, x:x+blocksize]	# 텍스쳐에서 해당 블록 return


# original 사용 함수
def findPatchBoth(refBlockLeft, refBlockTop, texture, blocksize, overlap, tolerance):
	'''
	Find best horizontal and vertical match from the texture
	사용: findPatchBoth(refBlockLeft, refBlockTop, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
								# openCV 경우 -> (rows, columns, channels) 튜플 보유
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# [0,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)
		rmsVal = ((texture[i:i+overlap, j:j+blocksize] - refBlockTop[-overlap:, :])**2).mean()	# (위의 이웃 블록의 오버랩 부분 - 각 블록의 위쪽 오버랩 부분) 제곱 의 평균
		rmsVal = rmsVal + ((texture[i:i+blocksize, j:j+overlap] - refBlockLeft[:, -overlap:])**2).mean()	# (왼쪽의 이웃 블록의 오버랩 부분 - 각 블록의 오른쪽 오버랩 부분) 제곱 의 평균
		if rmsVal > 0:
			errMat[i, j] = rmsVal	# 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것

	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기
	c = np.random.randint(len(y))	# random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
	y, x = y[c], x[c]	# 허용오차 안의 해당 에러중 랜덤하게 뽑음
	return texture[y:y+blocksize, x:x+blocksize]	# 텍스쳐에서 해당 블록 return


# original 사용 함수
def findPatchVertical(refBlock, texture, blocksize, overlap, tolerance):
	'''
	Find best vertical match from the texture
	사용: findPatchVertical(refBlock, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
								# openCV 경우 -> (rows, columns, channels) 튜플 보유
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# [0,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)
		rmsVal = ((texture[i:i+overlap, j:j+blocksize] - refBlock[-overlap:, :])**2).mean()	# (이웃 블록의 오버랩 부분 - 각 블록의 오버랩 부분) 제곱 의 평균
		if rmsVal > 0:
			errMat[i, j] = rmsVal	# 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것
	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기
	c = np.random.randint(len(y))	# random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
	y, x = y[c], x[c]	# 허용오차 안의 해당 에러중 랜덤하게 뽑음
	return texture[y:y+blocksize, x:x+blocksize]	# 텍스쳐에서 해당 블록 return


# original 사용 함수
def getMinCutPatchHorizontal(block1, block2, blocksize, overlap):
	'''
	Get the min cut patch done horizontally
	사용: getMinCutPatchHorizontal(refBlock, patchBlock, blocksize, overlap)
	'''
	err = ((block1[:, -overlap:] - block2[:, :overlap])**2).mean(2)	# mean(2)?? / ((두 블록의 오버랩 부분의 차) 제곱 ) 평균
	# maintain minIndex for 2nd row onwards and
	# -> E 구하는건 윗 행의 E 값들의 min 을 비교하기 때문에 두번째 행의 E 부터 가능하다는 뜻으로 이해
	minIndex = []
	E = [list(err[0])]	# 첫 행만 뽑아서 리스트로 만듬
						# [[0.0032859156734589266, 0.004070229398949124, 0.003967704728950406]] 형태

	for i in range(1, err.shape[0]):	# .shape[0] : 행의 개수
		# Get min values and args, -1 = left, 0 = middle, 1 = right
		e = [inf] + E[-1] + [inf]	# [inf, 0.0032859156734589266, 0.004070229398949124, 0.003967704728950406, inf] 형태
		e = np.array([e[:-2], e[1:-1], e[2:]])	# 배열 생성
												# [[       inf 0.04719211 0.04602845]
 												# [0.04719211 0.04602845 0.04679739]
     											# [0.04602845 0.04679739        inf]] 형태

		# Get minIndex
		minArr = e.min(0)	# e에서의 각 행의 최소 값 / [첫번째 행 최소 값, 두번째 행 최소값, 세번째 행 최소값]
							# 형태 : [0.22153531 0.12927848 0.12927848]
		minArg = e.argmin(0) - 1	# e.argmin : e에서 각 행의 최소값 위치 반환 -> [0,1,2] -1 -> [-1 , 0 , 1] / [첫번째 행 최소 값 위치, 두번째 행 최소값 위치, 세번째 행 최소값 위치]
		minIndex.append(minArg)	# 최소 위치 계속 추가 -> [1 1 0] [0 1 0] [1 0 -1] + + +
		# Set Eij = e_ij + min_
		Eij = err[i] + minArr	# minArr = min( E(i-1 , j-1) , E(i-1 , j), E(i-1 , j+1) )
		E.append(list(Eij))	# 식을 이용해 구한 err 값 첫 행만 뽑은 E에 추가
		# E 행개수 : n개 , minIndex 행개수 : n-1개
	# E 형태 :  [[0.01045751633986928, 0.02260156350121748, 0.008145585031398181], ... ,[0.376080994489299, 0.37763936947327953, 0.3876560297321543]]

	# Check the last element and backtrack to find path
	path = []
	minArg = np.argmin(E[-1])	# np.argmin: 최소값 인덱스 반환
								# 전체적으로 overlap 부분 오류에 대하여 모두 구한 E 모두에 젤 마지막 줄의 최소값의 위치 (ex) 0) / 0,1,2 중 최소인덱스 하나 입력됨
	path.append(minArg)	# path 에 넣어줌


	# Backtrack to min path
	for idx in minIndex[::-1]:	# 전체적으로 E 구할 때 2번째 행부터 마지막까지 한 행 당 [inf A B C] [A B C] [B C inf] 에 대하여 뒤에서부터 보는 배열 / [0 1 1] [-1 0 1] ...

		minArg = minArg + idx[minArg]	# 이해 필요??  / -1,0,1,2 중 하나의 값 나옴
										# idx 로 움직이며 , 이전 minArg 값으로 다음 값을 갱신함
		path.append(minArg)

	# Reverse to find full path
	path = path[::-1]	# 거꾸로 출력
	mask = np.zeros((blocksize, blocksize, block1.shape[2]))	# 0으로된 배열 생성 / .shape[2]: 컬러채널 / 3차원 [블록사이즈, 블록사이즈 , 컬러]
	for i in range(len(path)):
		mask[i, :path[i]+1] = 1	# path[i]+1] : 위치 값 넣어줄 때 -1 했었으므로 다시 0,1,2 형태로 만들기 위해서 1 더해줌

	resBlock = np.zeros(block1.shape)	# 블록과 같은 형태 0으로된 배열 -> 새로 끼울 블록 -> 왼쪽 경계 울퉁불퉁하게 만들어야함
	resBlock[:, :overlap] = block1[:, -overlap:]	# 왼쪽 처음에서 부터 overlap 부분까지 -> 기존  블록인 블록 1의 오른쪽 오버랩 부분을 대입
	resBlock = resBlock*mask + block2*(1-mask)	# 최종 새로운 블록 왼쪽 경계 = path 넣어준 마스크 곱함 + 새로 끼울 블록 2도 그 반대로 마스크가 생성되어 곱함
	# resBlock = block1*mask + block2*(1-mask)
	return resBlock

# original 사용 함수
def getMinCutPatchVertical(block1, block2, blocksize, overlap):	# horizontal 에서 인자 블록만 반시계 90도 돌려서 같은 계산 행함
	'''
	Get the min cut patch done vertically
	'''
	resBlock = getMinCutPatchHorizontal(np.rot90(block1), np.rot90(block2), blocksize, overlap)	# np.rot90 : 반시계방향으로 90도 회전 / horizontal 과 동일해짐
	return np.rot90(resBlock, 3)	# 이미 90도 돌린 상태로 계산 -> 원상복귀 -> 270 도 더 돌려서 360도 만들어줌

# original 사용 함수
def getMinCutPatchBoth(refBlockLeft, refBlockTop, patchBlock, blocksize, overlap):
	'''
	Find minCut for both and calculate
	'''
	err = ((refBlockLeft[:, -overlap:] - patchBlock[:, :overlap])**2).mean(2)	# mean(2)?? / ((왼쪽 기존블록과 새로운 패치블록의 오버랩 부분의 차) 제곱 ) 평균
	# maintain minIndex for 2nd row onwards and
	# -> E 구하는건 윗 행의 E 값들의 min 을 비교하기 때문에 두번째 행의 E 부터 가능하다는 뜻으로 이해
	minIndex = []
	E = [list(err[0])]	# 첫 행만 뽑아서 리스트로 만듬
						# [[0.0032859156734589266, 0.004070229398949124, 0.003967704728950406]] 형태

	for i in range(1, err.shape[0]):	# .shape[0] : 행의 개수
		# Get min values and args, -1 = left, 0 = middle, 1 = right
		e = [inf] + E[-1] + [inf]	# [inf, 0.0032859156734589266, 0.004070229398949124, 0.003967704728950406, inf] 형태
		e = np.array([e[:-2], e[1:-1], e[2:]])	# 배열 생성
												# [[       inf 0.04719211 0.04602845]
 												# [0.04719211 0.04602845 0.04679739]
     											# [0.04602845 0.04679739        inf]] 형태
		# Get minIndex
		minArr = e.min(0)	# e에서의 각 행의 최소 값 / [첫번째 행 최소 값, 두번째 행 최소값, 세번째 행 최소값]
							# 형태 : [0.22153531 0.12927848 0.12927848]
		minArg = e.argmin(0) - 1	# e.argmin : e에서 각 행의 최소값 위치 반환 -> [0,1,2] -1 -> [-1 , 0 , 1]
									# [첫번째 행 최소 값 위치, 두번째 행 최소값 위치, 세번째 행 최소값 위치]
		minIndex.append(minArg)	# 최소 위치 계속 추가 -> [1 1 0] [0 1 0] [1 0 -1] + + +
		# Set Eij = e_ij + min_
		Eij = err[i] + minArr	# minArr = min( E(i-1 , j-1) , E(i-1 , j), E(i-1 , j+1) )
		E.append(list(Eij))	# 식을 이용해 구한 err 값 첫 행만 뽑은 E에 추가
	# E 형태 :  [[0.01045751633986928, 0.02260156350121748, 0.008145585031398181], ... ,[0.376080994489299, 0.37763936947327953, 0.3876560297321543]]

	# Check the last element and backtrack to find path
	path = []
	minArg = np.argmin(E[-1])	# 전체적으로 overlap 부분 오류에 대하여 모두 구한 E 모두에 젤 마지막 줄의 최소값의 위치 (ex) 0) / 0,1,2 중 최소인덱스 하나 입력됨
	path.append(minArg)	# path 에 넣어줌

	# Backtrack to min path
	for idx in minIndex[::-1]:	# 전체적으로 E 구할 때 2번째 행부터 마지막까지 한 행 당 [inf A B C] [A B C] [B C inf] 에 대하여 뒤에서부터 보는 배열 / [0 1 1] [-1 0 1] ...
		minArg = minArg + idx[minArg]	# 이해 필요?? / -1,0,1,2 중 하나의 값 나옴
										# idx 로 움직이며 , 이전 minArg 값으로 다음 값을 갱신함
		path.append(minArg)

	# Reverse to find full path
	path = path[::-1]	# 거꾸로 출력
	# 마스크 만들기
	mask1 = np.zeros((blocksize, blocksize, patchBlock.shape[2]))	# 0으로된 배열 생성 / .shape[2]: 컬러채널 / 3차원 [블록사이즈, 블록사이즈 , 컬러]
	for i in range(len(path)):
		mask1[i, :path[i]+1] = 1	# path[i]+1] : 위치 값 넣어줄 때 -1 했었으므로 다시 0,1,2 형태로 만들기 위해서 1 더해줌


	#######################
	## Now for vertical one -> horizontal 하고 똑같이
	err = ((np.rot90(refBlockTop)[:, -overlap:] - np.rot90(patchBlock)[:, :overlap])**2).mean(2)	# mean(2)?? / ((반시계방향으로 회전시킨 두 블록의 차) 제곱 ) 평균

	# maintain minIndex for 2nd row onwards and
	# -> E 구하는건 윗 행의 E 값들의 min 을 비교하기 때문에 두번째 행의 E 부터 가능하다는 뜻으로 이해
	minIndex = []
	E = [list(err[0])]	# 첫 행만 뽑아서 리스트로 만듬
						# [[0.0032859156734589266, 0.004070229398949124, 0.003967704728950406]] 형태

	for i in range(1, err.shape[0]):	# .shape[0] : 행의 개수
		# Get min values and args, -1 = left, 0 = middle, 1 = right
		e = [inf] + E[-1] + [inf]	# [inf, 0.0032859156734589266, 0.004070229398949124, 0.003967704728950406, inf] 형태
		e = np.array([e[:-2], e[1:-1], e[2:]])	# 배열 생성
												# [[       inf 0.04719211 0.04602845]
 												# [0.04719211 0.04602845 0.04679739]
     											# [0.04602845 0.04679739        inf]] 형태
		# Get minIndex
		minArr = e.min(0)	# e에서의 각 행의 최소 값 / [첫번째 행 최소 값, 두번째 행 최소값, 세번째 행 최소값]
		minArg = e.argmin(0) - 1	# e.argmin : e에서 각 행의 최소값 위치 반환 -> [0,1,2] -1 -> [-1 , 0 , 1] / [첫번째 행 최소 값 위치, 두번째 행 최소값 위치, 세번째 행 최소값 위치]
		minIndex.append(minArg)	# 최소 위치 계속 추가 -> [1 1 0] [0 1 0] [1 0 -1] + + +
		# Set Eij = e_ij + min_
		Eij = err[i] + minArr	# minArr = min( E(i-1 , j-1) , E(i-1 , j), E(i-1 , j+1) )
		E.append(list(Eij))	# 식을 이용해 구한 err 값 첫 행만 뽑은 E에 추가

	# Check the last element and backtrack to find path
	path = []
	minArg = np.argmin(E[-1])	# 전체적으로 overlap 부분 오류에 대하여 모두 구한 E 모두에 젤 마지막 줄의 최소값의 위치 (ex) 0)
	path.append(minArg)	# path 에 넣어줌

	# Backtrack to min path
	for idx in minIndex[::-1]:	# 전체적으로 E 구할 때 2번째 행부터 마지막까지 한 행 당 [inf A B C] [A B C] [B C inf] 에 대하여 뒤에서부터 보는 배열 / [0 1 1] [-1 0 1] ...
		minArg = minArg + idx[minArg]	# 이해 필요?? /
		path.append(minArg)
	# Reverse to find full path
	path = path[::-1]	# 거꾸로 출력
	# 마스크 만들기!
	mask2 = np.zeros((blocksize, blocksize, patchBlock.shape[2]))	# 0으로된 배열 생성 / .shape[2]: 컬러채널 / 3차원 [블록사이즈, 블록사이즈 , 컬러]
	for i in range(len(path)):
		mask2[i, :path[i]+1] = 1	# path[i]+1] : 위치 값 넣어줄 때 -1 했었으므로 다시 0,1,2 형태로 만들기 위해서 1 더해줌
	mask2 = np.rot90(mask2, 3)	# 90도 반시계방향으로 돌려줬으므로 -> 원상복귀 -> 270 도 더 돌려서 360도로 만듬


	mask2[:overlap, :overlap] = np.maximum(mask2[:overlap, :overlap] - mask1[:overlap, :overlap], 0)	# np.maximum : 여러 array 사이에서 각 위치의 최대값
	# mask2 오버랩 제외부분 = [mask2 - mask1 의 각 최대값들의 배열0, mask2 - mask1 의 각 최대값들의 배열1, 0]

	# Put first mask
	resBlock = np.zeros(patchBlock.shape)
	resBlock[:, :overlap] = mask1[:, :overlap]*refBlockLeft[:, -overlap:]	# resBlock 에 오른쪽 오버랩 부분을 mask1 값도 곱해서 다시 대입
	resBlock[:overlap, :] = resBlock[:overlap, :] + mask2[:overlap, :]*refBlockTop[-overlap:, :]	# resBlock 에 위쪽 오버랩 부분을 mask2 값도 곱해서 다시 대입
	resBlock = resBlock + (1-np.maximum(mask1, mask2))*patchBlock	# 기존 패치블록도 마스크 반대값(반대로 울퉁불퉁 모양으로 자름) 해줘서 더함
	return resBlock

# original main 함수
def generateTextureMap(image, blocksize, overlap, outH, outW, tolerance):	# main.py에서 사용되는 메인. tolerance : 허용요차
	# 사용: generateTextureMap(image, block_size, overlap, outH, outW, args.tolerance)
	# ceil() : 소수점 자리의 숫자를 무조건 올리는 함수
	nH = int(ceil((outH - blocksize)*1.0/(blocksize - overlap)))	# 최종 이미지 크기에 오버랩 부분을 제외한 실제 블록들이 몇개 들어가는가?
	nW = int(ceil((outW - blocksize)*1.0/(blocksize - overlap)))	# 최종 이미지 크기에 오버랩 부분을 제외한 실제 블록들이 몇개 들어가는가?

	textureMap = np.zeros(((blocksize + nH*(blocksize - overlap)), (blocksize + nW*(blocksize - overlap)), image.shape[2]))
	# [(H기준 : nH(들어가는 블록개수) * (오버랩 뺀 블록실제사이즈) + 마지막에 오버랩 안되므로 블록 하나 더 사이즈) , (W기준 동일) , 색상] => 0으로 초기화
	# Starting index and block
	H, W = image.shape[:2]

	randH = np.random.randint(H - blocksize)  # 블록사이즈 한줄 뺀 값에서 랜덤한 값
	randW = np.random.randint(W - blocksize)  # 블록사이즈 한줄 뺀 값에서 랜덤한 값

	startBlock = image[randH:randH+blocksize, randW:randW+blocksize]	# 랜덤한 위치에서 시작하는 블록 사이즈만큼 잘라서 가져옴
	textureMap[:blocksize, :blocksize, :] = startBlock	# 0으로 초기화된 맵에서 첫번째 블록에 랜덤하게 가져온 블록 대입함

	# Fill the first row : 행(아래 위)
	for i, blkIdx in enumerate(range((blocksize-overlap), textureMap.shape[1]-overlap, (blocksize-overlap))):	# enumerate() : 인덱스와 원소 차례로 반환
		# 오버랩 부분 제외 블록 부분부터 ~ 오버랩 제외 열들까지 , 오버랩 제외한 블록사이즈만큼 옆으로 이동 (오른 -> 왼)

		# Find horizontal error for this block
		# Calculate min, find index having tolerance
		# Choose one randomly among them
		# blkIdx = block index to put in
		# blkIdx = 블록에서 오버랩 되는 부분 시작점 인덱스
		refBlock = textureMap[:blocksize, (blkIdx-blocksize+overlap):(blkIdx+overlap)]	#texturemap 의 한줄제외 모든 행에 대하여 열단위로 블록 한 칸만큼 계속 이동하면서 대입
		patchBlock = findPatchHorizontal(refBlock, image, blocksize, overlap, tolerance)	# 미리 만든 패치 찾는 함수
		minCutPatch = getMinCutPatchHorizontal(refBlock, patchBlock, blocksize, overlap)	# 미리 만든 최소 경로 찾는 함수
		textureMap[:blocksize, (blkIdx):(blkIdx+blocksize)] = minCutPatch	# 오버랩부분 경계선 최소경로로 자름
	print("{} out of {} rows complete...".format(1, nH+1))


	### Fill the first column 열 (오른 왼쪽)
	for i, blkIdx in enumerate(range((blocksize-overlap), textureMap.shape[0]-overlap, (blocksize-overlap))):	# # enumerate() : 인덱스와 원소 차례로 반환
		# 오버랩 부분 제외 블록 부분부터 ~ 오버랩 제외 행들까지 , 오버랩 제외한 블록사이즈만큼 옆으로 이동 (위 -> 아래)

		# Find vertical error for this block
		# Calculate min, find index having tolerance
		# Choose one randomly among them
		# blkIdx = block index to put in
		# blkIdx = 블록에서 오버랩 되는 부분 시작점 인덱스
		refBlock = textureMap[(blkIdx-blocksize+overlap):(blkIdx+overlap), :blocksize]	#texturemap 의 한줄제외 모든 열에 대하여 행단위로 블록 한 칸만큼 계속 이동하면서 대입
		patchBlock = findPatchVertical(refBlock, image, blocksize, overlap, tolerance)	# 미리 만든 패치 찾는 함수
		minCutPatch = getMinCutPatchVertical(refBlock, patchBlock, blocksize, overlap)	# 미리 만든 최소 경로 찾는 함수
		textureMap[(blkIdx):(blkIdx+blocksize), :blocksize] = minCutPatch	# 오버랩부분 경계선 최소경로로 자름

	### Fill in the other rows and columns
	for i in range(1, nH+1):
		for j in range(1, nW+1):
			# Choose the starting index for the texture placement
			blkIndexI = i*(blocksize-overlap)
			blkIndexJ = j*(blocksize-overlap)
			# Find the left and top block, and the min errors independently
			refBlockLeft = textureMap[(blkIndexI):(blkIndexI+blocksize), (blkIndexJ-blocksize+overlap):(blkIndexJ+overlap)]
			refBlockTop  = textureMap[(blkIndexI-blocksize+overlap):(blkIndexI+overlap), (blkIndexJ):(blkIndexJ+blocksize)]

			patchBlock = findPatchBoth(refBlockLeft, refBlockTop, image, blocksize, overlap, tolerance)
			minCutPatch = getMinCutPatchBoth(refBlockLeft, refBlockTop, patchBlock, blocksize, overlap)

			textureMap[(blkIndexI):(blkIndexI+blocksize), (blkIndexJ):(blkIndexJ+blocksize)] = minCutPatch

			# refBlockLeft = 0.5
			# textureMap[(blkIndexI):(blkIndexI+blocksize), (blkIndexJ-blocksize+overlap):(blkIndexJ+overlap)] = refBlockLeft
			# textureMap[(blkIndexI-blocksize+overlap):(blkIndexI+overlap), (blkIndexJ):(blkIndexJ+blocksize)] = [0.5, 0.6, 0.7]
			# break
		print("{} out of {} rows complete...".format(i+1, nH+1))
		# break

	return textureMap
#####################################################
#####################################################
#####################################################

# 회전 텍스처 합성 부분 #########################
# 회전 텍스처 합성 사용 함수
def r_findPatchHorizontal(refBlock, texture, blocksize, overlap, tolerance, mask):	# tolerance : 허용오차
	'''
	Find best horizontal match from the texture
	사용: findPatchHorizontal(refBlock, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성 / inf 는 왜더하는지는 모르겠음???
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# openCV 경우 -> (rows, columns, channels) 튜플 보유,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)

		if (mask[i:i + blocksize, j:j + blocksize] == 1).all():
			rmsVal = ((texture[i:i + blocksize, j:j + overlap] - refBlock[:, -overlap:]) ** 2).mean()  # (이웃 블록의 오버랩 부분 - 각 블록의 오버랩 부분) 제곱 의 평균
			if rmsVal > 0:
				errMat[i, j] = rmsVal  # 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것
	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E 고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기


	while (True):
		c = np.random.randint(len(y))	# random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
		yy, xx = y[c], x[c]	# 허용오차 안의 해당 에러 중 랜덤하게 뽑음
		if (mask[yy:yy+blocksize, xx:xx+blocksize]==1).all():
			break

	return texture[yy:yy+blocksize, xx:xx+blocksize]	# 텍스쳐에서 해당 블록 return


# 회전 텍스처 합성 사용 함수
def r_findPatchBoth(refBlockLeft, refBlockTop, texture, blocksize, overlap, tolerance, mask):
	'''
	Find best horizontal and vertical match from the texture
	사용: findPatchBoth(refBlockLeft, refBlockTop, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
								# openCV 경우 -> (rows, columns, channels) 튜플 보유
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# [0,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)
		if (mask[i:i+blocksize, j:j+blocksize] == 1).all():
			rmsVal = ((texture[i:i+overlap, j:j+blocksize] - refBlockTop[-overlap:, :])**2).mean()	# (위의 이웃 블록의 오버랩 부분 - 각 블록의 위쪽 오버랩 부분) 제곱 의 평균
			rmsVal = rmsVal + ((texture[i:i+blocksize, j:j+overlap] - refBlockLeft[:, -overlap:])**2).mean()	# (왼쪽의 이웃 블록의 오버랩 부분 - 각 블록의 오른쪽 오버랩 부분) 제곱 의 평균
			if rmsVal > 0:
				errMat[i, j] = rmsVal	# 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것
	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기
	while (True):
		c = np.random.randint(len(y))  # random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
		yy, xx = y[c], x[c]  # 허용오차 안의 해당 에러 중 랜덤하게 뽑음
		if (mask[yy:yy + blocksize, xx:xx + blocksize] == 1).all():
			break

	return texture[yy:yy+blocksize, xx:xx+blocksize]	# 텍스쳐에서 해당 블록 return


# 회전 텍스처 합성 사용 함수
def r_findPatchVertical(refBlock, texture, blocksize, overlap, tolerance, mask):
	'''
	Find best vertical match from the texture
	사용: findPatchVertical(refBlock, image, blocksize, overlap, tolerance)
	'''
	H, W = texture.shape[:2]	# 튜플 압축 풀기 -> 해당 texture 의 rows, columns  값 추출
								# openCV 경우 -> (rows, columns, channels) 튜플 보유
	errMat = np.zeros((H-blocksize, W-blocksize)) + inf	# np.zeros : 0으로 채워진 array 생성 / [[W-blocksize 만큼]*H-blocksize만큼] 0으로된 2차원 배열 생성
	for i, j in product(range(H-blocksize), range(W-blocksize)):	# product : 중복 순열 , 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 / range : 0~해당 값까지
																	# [0,1,2, ... ,H-blocksize] [0,1,2, ... , W-blocksize] => (0,0),(0,1)..(0,W-blocksize),(1,0),...,(H-blocksize,W-blocksize)
		if (mask[i:i+blocksize, j:j+blocksize] == 1).all():
			rmsVal = ((texture[i:i+overlap, j:j+blocksize] - refBlock[-overlap:, :])**2).mean()	# (이웃 블록의 오버랩 부분 - 각 블록의 오버랩 부분) 제곱 의 평균
			if rmsVal > 0:
				errMat[i, j] = rmsVal	# 텍스쳐 크기에서 블록사이즈만큼 한줄 작아진 배열에 대입

	minVal = np.min(errMat)	# 에러범위 값 중 가장 작은 것
	y, x = np.where(errMat < (1.0 + tolerance)*(minVal))	# np.where: 조건에 맞는 위치 인덱스 찾기 / 해당 허용오차보다 작은 E고름
															# y : [뽑힌 원소 각각 행 어디인지]
															# x : [뽑힌 원소 각각 열 어디인지] - (y,x) 둘이 이어서 위치 찾기

	while (True):
		c = np.random.randint(len(y))	# random.randint() : [최소값, 최대값) 랜덤 정수 / 0~len(y) 전까지 / len(y) == len(x)
		yy, xx = y[c], x[c]	# 허용오차 안의 해당 에러 중 랜덤하게 뽑음
		if (mask[yy:yy+blocksize, xx:xx+blocksize]==1).all():
			break

	return texture[yy:yy+blocksize, xx:xx+blocksize]	# 텍스쳐에서 해당 블록 return

# 회전 텍스처 합성 메인 함수
def r_generateTextureMap(image, blocksize, overlap, outH, outW, tolerance, mask ) :	# 회전이미지에서 검은부분 합성으로 채우기
	# 사용: generateTextureMap(image, block_size, overlap, outH, outW, args.tolerance)
	# ceil() : 소수점 자리의 숫자를 무조건 올리는 함수

	nH = int(ceil((outH - blocksize)*1.0/(blocksize - overlap)))	# 최종 이미지 크기에 오버랩 부분을 제외한 실제 블록들이 몇개 들어가는가?
	nW = int(ceil((outW - blocksize)*1.0/(blocksize - overlap)))	# 최종 이미지 크기에 오버랩 부분을 제외한 실제 블록들이 몇개 들어가는가?

	textureMap = np.zeros(((blocksize + nH*(blocksize - overlap)), (blocksize + nW*(blocksize - overlap)), image.shape[2]))
	# [(H기준 : nH(들어가는 블록개수) * (오버랩 뺀 블록실제사이즈) + 마지막에 오버랩 안되므로 블록 하나 더 사이즈) , (W기준 동일) , 색상] => 0으로 초기화
	
	# Starting index and block
	H, W = image.shape[:2]

	while (True):  # do-while 문
		randH = np.random.randint(H - blocksize)  # 블록사이즈 한줄 뺀 값에서 랜덤한 값
		randW = np.random.randint(W - blocksize)  # 블록사이즈 한줄 뺀 값에서 랜덤한 값

		if (mask[randH:randH + blocksize, randW:randW + blocksize] == 1).all():  # 로테이션 이미지 존재한는 부분일 때의 random 값 뽑아내기
			break

	startBlock = image[randH:randH + blocksize, randW:randW + blocksize]  # 랜덤한 위치에서 시작하는 블록 사이즈만큼 잘라서 가져옴
	textureMap[:blocksize, :blocksize, :] = startBlock  # 0으로 초기화된 맵에서 첫번째 블록에 랜덤하게 가져온 블록 대입함

	# Fill the first row : 행(아래 위)
	for i, blkIdx in enumerate(range((blocksize - overlap), textureMap.shape[1] - overlap, (blocksize - overlap))):  # enumerate() : 인덱스와 원소 차례로 반환
		# 오버랩 부분 제외 블록 부분부터 ~ 오버랩 제외 열들까지 , 오버랩 제외한 블록사이즈만큼 옆으로 이동 (오른 -> 왼)

		# Find horizontal error for this block
		# Calculate min, find index having tolerance
		# Choose one randomly among them
		# blkIdx = block index to put in
		# blkIdx = 블록에서 오버랩 되는 부분 시작점 인덱스
		refBlock = textureMap[:blocksize, (blkIdx - blocksize + overlap):(blkIdx + overlap)]  # texturemap 의 한줄제외 모든 행에 대하여 열단위로 블록 한 칸만큼 계속 이동하면서 대입
		patchBlock = r_findPatchHorizontal(refBlock, image, blocksize, overlap, tolerance, mask)  # 미리 만든 패치 찾는 함수
		minCutPatch = getMinCutPatchHorizontal(refBlock, patchBlock, blocksize, overlap)  # 미리 만든 최소 경로 찾는 함수
		textureMap[:blocksize, (blkIdx):(blkIdx + blocksize)] = minCutPatch  # 오버랩부분 경계선 최소경로로 자름
	print("{} out of {} rows complete...".format(1, nH + 1))

	### Fill the first column 열 (오른 왼쪽)
	for i, blkIdx in enumerate(range((blocksize - overlap), textureMap.shape[0] - overlap, (blocksize - overlap))):  # # enumerate() : 인덱스와 원소 차례로 반환
		# 오버랩 부분 제외 블록 부분부터 ~ 오버랩 제외 행들까지 , 오버랩 제외한 블록사이즈만큼 옆으로 이동 (위 -> 아래)

		# Find vertical error for this block
		# Calculate min, find index having tolerance
		# Choose one randomly among them
		# blkIdx = block index to put in
		# blkIdx = 블록에서 오버랩 되는 부분 시작점 인덱스
		refBlock = textureMap[(blkIdx - blocksize + overlap):(blkIdx + overlap), :blocksize]  # texturemap 의 한줄제외 모든 열에 대하여 행단위로 블록 한 칸만큼 계속 이동하면서 대입
		patchBlock = r_findPatchVertical(refBlock, image, blocksize, overlap, tolerance, mask)  # 미리 만든 패치 찾는 함수
		minCutPatch = getMinCutPatchVertical(refBlock, patchBlock, blocksize, overlap)  # 미리 만든 최소 경로 찾는 함수
		textureMap[(blkIdx):(blkIdx + blocksize), :blocksize] = minCutPatch  # 오버랩부분 경계선 최소경로로 자름

	### Fill in the other rows and columns
	for i in range(1, nH + 1):
		for j in range(1, nW + 1):
			# Choose the starting index for the texture placement
			blkIndexI = i * (blocksize - overlap)
			blkIndexJ = j * (blocksize - overlap)
			# Find the left and top block, and the min errors independently
			refBlockLeft = textureMap[(blkIndexI):(blkIndexI + blocksize), (blkIndexJ - blocksize + overlap):(blkIndexJ + overlap)]
			refBlockTop = textureMap[(blkIndexI - blocksize + overlap):(blkIndexI + overlap), (blkIndexJ):(blkIndexJ + blocksize)]

			patchBlock = r_findPatchBoth(refBlockLeft, refBlockTop, image, blocksize, overlap, tolerance, mask)
			minCutPatch = getMinCutPatchBoth(refBlockLeft, refBlockTop, patchBlock, blocksize, overlap)

			textureMap[(blkIndexI):(blkIndexI + blocksize), (blkIndexJ):(blkIndexJ + blocksize)] = minCutPatch

		# refBlockLeft = 0.5
		# textureMap[(blkIndexI):(blkIndexI+blocksize), (blkIndexJ-blocksize+overlap):(blkIndexJ+overlap)] = refBlockLeft
		# textureMap[(blkIndexI-blocksize+overlap):(blkIndexI+overlap), (blkIndexJ):(blkIndexJ+blocksize)] = [0.5, 0.6, 0.7]
		# break
		print("{} out of {} rows complete...".format(i + 1, nH + 1))
	# break

	return textureMap

#################################################
#################################################
#################################################

########################################
# 회전 텍스처 합성 부분 #########################

# 텍스처 회전 시 이미지 존재하지 않는 부분(0)을 마스크로 만들기
def MakeMask(h, w, r_seta):
	# make mask 
	mask_black = np.ones((h, w, 3))
	if(r_seta%90 != 0):
		def get_crosspt(y1, x21, y21, x22, y22):
			m2 = round((y22 - y21) / (x22 - x21) ,3)
			a = y1
			x1 = x21
			y1 = y21
			Y = a
			X = round( ((a-y1)/m2)+x1 ,3)

			return X, Y
		
		a = w
		d = round(a*math.sqrt(2)/2, 3)
		de = math.radians(r_seta%90)
		r45 = math.radians(45)

		L1 = a//2
		L2s1x = d * round(math.cos(r45+de),3)
		L2s1y = d * round(math.sin(r45 + de),3)
		L2s2x = d * round(math.cos(r45-de),3)
		L2s2y = -1 * (d * round(math.sin(r45 - de),3))
		X2,Y2 = get_crosspt(L1, L2s1x, L2s1y, L2s2x, L2s2y)

		L3s1x = d * round(math.cos(r45 + de), 3)
		L3s1y = d * round(math.sin(r45 + de), 3)
		L3s2x = -1 * (d * round(math.cos(r45 - de), 3))
		L3s2y = d * round(math.sin(r45 - de), 3)
		X3, Y3 = get_crosspt(L1, L3s1x, L3s1y, L3s2x, L3s2y)

		Line1 = int(X3+L1)
		Line2 = int(X2-X3)
		Line3 = int(L1-X2)
		overplus = 3

		# 왼쪽 위 부분
		for x in range((Line1+1)+overplus):  
			equation1 = ceil((-1) * (Line3 / Line1) * x + Line3)
			for y in range(equation1+overplus):
				mask_black[y, x] = 0
		# 왼쪽 아래 부분
		for x in range((Line3+1)+overplus):
			equation2 = ceil((Line1 / Line3) * x + (Line2 + Line3))
			for y in range(equation2-overplus,a):
				mask_black[y, x] = 0
		# 오른쪽 위 부분
		for x in range((a-Line3-1)-overplus,a):
			equation3 = ceil((Line1 / Line3) * (x - (Line1 + Line2)) + (Line2 + Line3) + (-1) * (Line2 + Line3))
			for y in range(equation3+overplus):
				mask_black[y, x] = 0
		# 오른쪽 아래 부분
		for x in range((a-Line1-1)-overplus,a): 
			equation4 = ceil((-1) * (Line3 / Line1) * (x - (Line2 + Line3)) + Line3 + (a-Line3))
			for y in range(equation4-overplus,a):
				mask_black[y, x] = 0

	return mask_black


###########
# 회전 예제 이미지 생성
def RotateExImgs(image, rotate_num, blocksize, overlap, tolerance, outH, outW):  # 방향성 더해주기 위한 내가만든 함수
	# 이미지의 크기를 잡고 이미지의 중심을 계산합니다.
	(h, w) = image.shape[:2]
	(cX, cY) = (w // 2, h // 2)
	results = []

	for i in range(1,rotate_num+1):
		imax = rotate_num
		r_seta = i / imax * 360

		# 이미지의 중심을 중심으로 이미지를 r_seta도 회전합니다.
		M = cv2.getRotationMatrix2D((cX, cY), r_seta, 1.0)	# cv2.getRotationMatrix2D(회전중심좌표(x,y 튜플), 회전각도, 스케일)
		rotated_seta = cv2.warpAffine(image, M, (h, w))	# cv2.warpAffine(src 원본이미지, M 아핀 맵 행렬, dsize 출력 이미지 크기) : 회전 변환을 계산

		mask = MakeMask(h, w, r_seta)

		# rotation -> 검은 삼각형 부분 => 합성 #########
		r_texture_black = r_generateTextureMap(rotated_seta, blocksize, overlap, outH, outW, tolerance, mask)	# 방향성 고려해서 새로 합성한 후보이미지
		r_texture_black = r_texture_black[:outH,:outW]

		results.append(r_texture_black)
	return results
