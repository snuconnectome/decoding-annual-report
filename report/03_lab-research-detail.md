# 디코딩과제 3년차 — Lab별 연구 상세

> **목적**: 평가단 발표 슬라이드 재구성의 원천 자료. 4개 연구팀(이상아/최형진/차지욱/문태섭 Lab)의 3년차 수행 내용을 교수급 granularity (실험 설계·뇌영역·바이오마커·수치)로 정리.
>
> **출처**:
> - 공식 제출본 (Google Docs `1TwvN09TGro2j4c2HDhWH-ldSVNh7wBz_f7irmyw64Bw`, 2025-12-08, 98p)
> - 차지욱 Lab ephys FM 슬라이드 (Google Slides `1LTc1e...`, 2026-02-19)
> - 문태섭 Lab SEED poster (PPTX `15mYsq...`, 2026-04-22)
> - 최형진 Lab BK21 자체평가 (Google Sheet `1lLcfs...`, 2025-10-16)
> - 리포 자료: `data/*.yaml`, `slides/storyboard.md`
>
> **정합성 노트**: 공식 제출본은 "세부연구 N" 라벨만 사용하며 Lab 소속을 명시하지 않음. 본 문서의 Lab 귀속은 모델·모달리티·주제 기반 추정이며, 평가단 질의 시 구두 보완 가능.

---

## 0.1 용어 사전 (약어 풀이)

본 보고서·슬라이드는 **약어 없음 정책 (no-acronym policy)** 을 따른다. 모든 전문용어는 첫 등장 시 풀네임 + (원어 약어) 형식으로 기술한다.

### 뇌영상·전기생리 모달리티
- **기능적 자기공명영상 (fMRI)**: 뇌 활동을 혈류·산소 변화로 간접 측정하는 영상 기법
- **구조적 자기공명영상 (sMRI)**: 뇌 해부학적 구조를 보는 영상 기법
- **휴지기 기능적 자기공명영상 (rsfMRI)**: 과제 없이 쉬는 상태의 fMRI
- **뇌전도 (EEG)**: 두피 전극으로 측정하는 대뇌 피질 전기 활동
- **두개내 뇌전도 (iEEG)**: 뇌 표면 또는 내부에 직접 삽입한 전극으로 측정
- **심전도 (ECG)**: 심장 전기 활동
- **확산텐서영상 (DTI)**: 백질 섬유의 방향·구조 영상

### 주요 뇌영역
- **전대상피질 (ACC)**: 주의·갈등·정서 조절 영역. 복측(ventral)/배측(dorsal) 기능 분리 있음
- **기본모드 네트워크 (DMN)**: 쉴 때 활성화되는 자기참조·기억 관련 대규모 네트워크
- **후대상피질 (PCC)**: 기억 인출·자기 인식 관련
- **쐐기앞소엽 (precuneus)**: 일화기억·시공간 처리
- **안와전두피질 (OFC)**: 가치 평가·의사결정
- **해마 하위영역 CA2/3 + 치상회 (CA23DG)**: 패턴 분리·맥락 부호화 핵심
- **해마 CA1**: 맥락 연합·공간 기억 인출
- **측후각피질 (PrC)**: 물체 기억 처리
- **쐐기앞소엽 아래 해마하부 (subiculum)**: 해마 출력 영역, 공간 경계 감지
- **복측피개부 (VTA)**: 중뇌의 도파민 뉴런 기원 영역
- **측좌핵 (NAc)**: 보상·동기 회로 중심
- **중앙편도체 (CeA)**: 혐오·부정적 정서 처리
- **외측시상하부 (LH)**: 섭식·각성 조절
- **시상하부 활꼴핵 (ARC)**: 배고픔·대사 조절 중추

### 기계학습 모델·방법
- **SwiFT (Swin Transformer for fMRI)**: 차지욱 Lab의 fMRI 파운데이션 모델
- **SwiFT-IO**: SwiFT + Perceiver IO 인코더로 시계열 디코딩 확장
- **다중 주파수 대역 뇌 네트워크 (MBBN, Multi Band Brain Net)**: fMRI 신호를 주파수별 분리해 처리
- **NeuroMamba**: Mamba2 상태공간 모델 기반 fMRI 파운데이션
- **TabLeT**: fMRI 3D 볼륨을 2차원 오토인코더로 토큰화한 트랜스포머
- **잠재 확산 트랜스포머 (Latent Diffusion Transformer)**: 4차원 fMRI 생성 모델
- **DIVER-1**: 차지욱 Lab의 두개내 뇌전도·뇌전도 파운데이션 모델
- **POYO 기반 자기지도학습 (POYO-SSL)**: 동물 칼슘이미징용 세포 패턴 인식형 자기지도학습
- **시각-언어 모델 (VLM, Vision-Language Model)**: 이미지와 텍스트를 동일 임베딩 공간으로
- **시각 뇌 디코딩 시맨틱 평가 (SEED, Semantic Evaluation for Visual Brain Decoding)**: 문태섭 Lab 신규 평가 체계
- **자기지도학습 (SSL, Self-Supervised Learning)**: 레이블 없는 데이터로 표현 학습
- **사전학습 (Pre-training) → 전이학습 (Transfer Learning)**: 대규모 사전학습 후 특정 과제 적응
- **최대 업데이트 파라미터화 (muP)**: 거대 모델에도 안정적 하이퍼파라미터 전이 기법
- **신경 방사장 (NeRF, Neural Radiance Fields)**: 3차원 장면을 주파수 기반으로 표현

### 통계·평가 지표
- **결정계수 (R²)**: 0~1 범위. 1.0 = 완벽 예측, 0 = 평균 예측 수준, 음수 = 평균보다 나쁨
- **평균제곱오차 (MSE)**: 예측 오차의 제곱 평균. 낮을수록 우수
- **평균절대오차 (MAE)**: 예측 오차의 절댓값 평균. 낮을수록 우수
- **구조적 유사도 지수 (SSIM)**: 0~1. 1.0 = 두 이미지 완전 일치
- **F1 점수**: 정밀도와 재현율의 조화평균. 0~1, 1.0 = 완벽
- **당시 최고 성능 (SOTA, State-of-the-Art)**: 해당 벤치마크에서 발표 시점 최고 기록
- **일반선형모형 (GLM)**: fMRI 활성 통계 분석 표준 방법
- **선형혼합효과모형 (LMM)**: 개인차·반복측정을 반영한 회귀
- **독립성분분석 (ICA)**: 신호를 통계적 독립 성분으로 분해
- **유의확률 (p-value)**: 통상 p < 0.05 = 통계적 유의
- **표상적 유사도 분석 (RSA, Representational Similarity Analysis)**: 뇌 활동 패턴 간 유사도 비교
- **피험자 간 표상적 유사도 분석 (IS-RSA)**: 같은 자극에 대한 개인 간 표상 유사도

### 데이터셋
- **영국 바이오뱅크 (UK Biobank, UKB)**: 영국 50만 명 + 이상 대규모 코호트 (뇌영상 10만+)
- **인간 커넥톰 프로젝트 (HCP, Human Connectome Project)**: 1,200명 고해상도 뇌영상·행동
- **청소년기 뇌 인지 발달 연구 (ABCD, Adolescent Brain Cognitive Development)**: 11,000명+ 종단
- **Healthy Brain Network (HBN)**: 아동·청소년 뇌영상·정신건강 코호트
- **국제정서감정자극시스템 (IAPS, International Affective Picture System)**: 정서 유도 표준 이미지
- **알츠하이머병 신경영상 이니셔티브 (ADNI)**: 알츠하이머 종단 뇌영상 코호트
- **Allen Brain Observatory**: 동물 시각 자극-칼슘이미징 표준 데이터셋
- **Neuroprobe**: iEEG 디코딩 벤치마크 (15개 청각·시각·언어 과제)

### 임상 진단
- **주의력결핍 과잉행동장애 (ADHD)**
- **자폐스펙트럼장애 (ASD)**
- **경도인지장애 (MCI, Mild Cognitive Impairment)**: 치매 전 단계
- **안정형·진행형 경도인지장애 (sMCI·pMCI)**: 알츠하이머 전환 여부
- **알츠하이머병 (AD)**
- **간이정신상태검사 (MMSE)**: 인지기능 선별 검사
- **임상치매평가척도 점수 합계 (CDR-SB)**: 치매 중증도 평가
- **상태-특성 불안 척도 (STAI)**: 불안 수준 설문
  - **STAI-X1**: 상태 불안(State) 하위척도 — 현재 느끼는 불안
- **우울증 (Depression)** / **불안 (Anxiety)**

### 신경약리·분자
- **글루카곤 유사 펩타이드-1 (GLP-1)**: 혈당·섭식 조절 호르몬, 비만치료제 타겟
- **GLP-1 수용체 (Glp1R)**: GLP-1이 결합하는 세포막 단백질
- **엑센딘-4 (Exendin-4)**: GLP-1 수용체 작용제
- **아데노연관바이러스 (AAV, Adeno-Associated Virus)**: 유전자 전달 벡터
- **도파민 수송체 (DAT)**: 도파민 회수 단백질
- **DAT-cre 마우스**: DAT 발현 뉴런만 유전자 조작 가능한 형질전환 마우스
- **광유전학 (Optogenetics)**: 빛에 반응하는 단백질로 특정 뉴런 제어
- **칼슘이미징 (Calcium Imaging)**: 신경 활동을 형광 칼슘 센서로 측정
- **fiber photometry**: 광섬유로 살아있는 뇌의 신경 활동 실시간 측정
- **화학유전학 (Chemogenetics)**: 인공 수용체와 약물로 뉴런 제어
- **초음파 발성 (USV, Ultrasonic Vocalization)**: 설치류의 초음파 소리 (정서 지표)
- **다중화 오류보정 형광 원위치 혼성화 (MERFISH)**: 단일세포 공간 전사체 기법
- **단일세포 RNA 시퀀싱 (scRNA-seq)**: 개별 세포 유전자 발현 측정
- **DeepLabCut**: 딥러닝 기반 동물 행동 자세 추정 도구

### 응용·인터페이스
- **뇌-컴퓨터 인터페이스 (BCI, Brain-Computer Interface)**: 뇌 신호로 외부 장치 제어
- **가상현실 (VR, Virtual Reality)**
- **확산 모델 (Diffusion Model)**: 노이즈 역변환 기반 생성 AI

### 학술대회·기관
- **서울대학교 (SNU)**
- **브룩헤이븐 국립연구소 (BNL, Brookhaven National Lab)**
- **국제 머신러닝 학술대회 (ICML)**
- **국제 학습표현 학술대회 (ICLR)**
- **컴퓨터비전·패턴인식 학술대회 (CVPR)**
- **유럽 컴퓨터비전 학술대회 (ECCV)**
- **AAAI 인공지능 학회 (AAAI)**
- **인지신경과학 학술대회 (CCN)**
- **한국뇌신경과학회 (KSBNS)**

---

## 0.2 수치 해석 가이드 (평가단 참조)

| 원 수치 | 의미 해석 |
|---|---|
| R² = 0.96 | 결정계수 0.96 — 정서가 예측이 실제 값의 분산의 96%를 설명. 1.0이 완벽이므로 매우 우수 |
| SSIM = 0.593 | 구조적 유사도 0.593 — 복원 이미지가 원본과 약 59% 구조 일치 (1.0이 완전 일치) |
| F1 = 0.9 | F1 점수 0.9 — 정밀도와 재현율의 조화평균 0.9 (1.0이 완벽) |
| +12~13% | 기존 학습 방식(무학습 시작) 대비 12~13%포인트 성능 향상 |
| +14.4% | 언어-뇌영상 정렬에서 기존 최고 모델(Antonello et al.) 대비 정확도 14.4%포인트 향상 |
| 94.9% | HCP 1,200명 뇌영상으로 남녀 성별 분류 정확도 94.9% |
| +7.6% | SwiFT 모델이 HCP 성별 분류에서 이전 최고 모델보다 7.6%포인트 향상 |
| 88억 (8.8B) 파라미터 | 모델의 학습 가능 변수 88억 개 — 뇌영상 파운데이션 모델 중 최대 규모 |
| 5,300시간 (5.3k hrs) iEEG | 두개내 뇌전도 신호 누적 5,300시간 — ephys 분야 최대 규모 |
| 54,000시간 (54k hrs) EEG | 두피 뇌전도 신호 누적 54,000시간 |
| 17,700명 피험자 · 160만 채널-시간 | 전체 코퍼스 환자 수 × 전극별 기록 시간의 곱 |
| 50,000시간 | DIVER-2 로드맵 — 현재 5,300에서 10배 확장 |
| 22,000 판단 (22K) | 22명 평가자 × 1,000 이미지쌍 = 22,000건의 인간 품질 판단 |
| n = 92 | 참가자 92명 |
| 32 채널 · 2,048 Hz | 두피 EEG 32개 전극에서 초당 2,048회 샘플링 |
| p = 0.010 | 유의확률 0.010 — 통상 p < 0.05가 유의이므로 유의한 차이 |
| p = 0.002, 0.003 | 유의확률 0.002와 0.003 — 매우 유의한 차이 |
| 10-15% (chance 4%) | 디코딩 정확도 10-15%로 무작위 수준 4%보다 2-4배 높음 |
| 연산량 −46.5% | 기존 모델 대비 부동소수점 연산량 46.5% 감소 (효율 향상) |
| 1.98× 데이터 효율 | 같은 성능에 기존 방식보다 2배 적은 데이터로 달성 |
| 13M (13 million) 파라미터 | 1,300만 개 파라미터 — 비교 모델 BrainBERT 4,300만 · PopT 6,300만 능가 |
| 1e20 FLOPs | 10의 20제곱 부동소수점 연산 — GPT-1의 2배, 이전 ephys 최고 모델의 77배 컴퓨팅 |
| 30초 · 5/10/20 Hz | 30초 동안 초당 5회 · 10회 · 20회 빈도 광자극 |
| 594 nm | 파장 594 나노미터 적색광 (광유전학 자극용) |
| IF 26.3 · IF 12.9 등 | 영향력 지수 (Impact Factor) — 학술지의 연간 인용 빈도 |

---

## 0. 총람 — 4개 Lab × 평가항목 매핑

| Lab | 주요 모달리티 | 평가항목 | 3년차 핵심 성과 | 대표 지표 |
|---|---|---|---|---|
| **이상아 Lab** | 인간 fMRI·EEG, 해마·정서 | #1 (25%) | MixedEmo n=92, 해마 하위영역 OCAT, 가상공간 EEG sequential reactivation | fMRI 감정 연합 디코딩 10~15% (chance 4%) |
| **최형진 Lab** | 동물 칼슘이미징·광유전학 | #1 + 세부연구 5 | 3D 골격 DB, VTA-NAc two-site 광유전학, 편도체 표정-뉴런 정서 디코딩(차지욱 공동) | 자유 행동 설치류 멀티뷰 트래킹, 594nm DAT-cre 광자극 |
| **차지욱 Lab** | fMRI·EEG·iEEG 파운데이션 + 임상 | #2 + #4 (25%×2) | SwiFT 8.8B·DIVER-1·MBBN·NeuroMamba·POYO-SSL·Language-Brain·RYM·CEBRA·TabLeT | SwiFT-IO R²=0.96, DIVER-1 5.3k iEEG+54k EEG hrs, Language-Brain +14.4% |
| **문태섭 Lab** | Vision-Language + Quantum ML | #5 (25%) | SEED 평가 체계, VLM 다중 모달리티, Quantum Time-series Transformer | 22K 판단 × 5 SOTA 디코더 평가, LLaVA-Next-Interleave |

**합계 달성도**: 97.5% (4개 평가항목 × 각 25% 재분배, 원 평가항목 #3 신경과학 메커니즘은 본문에 수행되었으나 성과표에서 별도 평가 누락 — 4차년도 평가로 이월)

**대규모 데이터셋**: 동물 표정·음성 3,000건 이상 · 인간 뇌영상 500명 이상

---

## 1. 이상아 Lab — 인간 기억·정서 fMRI/EEG (평가항목 #1)

### 1.1 MixedEmo fMRI — 장소-감정 연합 기억 (n=92)

**연구 질문**: 동일한 장소에서 일어나는 두 감정 사건이 어떻게 연합되어 지각·인출되는가? 감정가의 변화(valence shift)는 대규모 뇌 네트워크에서 어떻게 표상되는가?

**설계**:
- **자극**: 장소(Scene, 흑백 80가지) × 감정자극(Cue, IAPS에서 추출 160가지)
- **5개 감정 조건**: 중립-중립, 부정-부정, 긍정-긍정, 긍정-부정, 부정-긍정
- **참가자**: 총 n=92 (전년 n=82에서 증가), 분석 완료 n=62
- **분석**: FMRIPREP 전처리 · MATLAB 사후 · GLM + 선형혼합효과모델(LMM)

**결과** (공식 제출본 인용):
- **지각 단계**: 감정자극 연합(1Emo, 2Emo) 시 **내측두엽 편도체** 및 **주목 관련 전두/두정엽** 활성
- **인출 단계**: 감정 연합기억 인출(2Loc) 시 **디폴트 모드 네트워크(DMN)** 활성
- **대규모 네트워크**: Fronto-parietal · dorsal attention · ventral attention · salience network 패턴
- **ACC 하위영역 해리**: 복측 rostral ACC — 외부 감정자극 부정적 반응 · 배측 ACC — 내부 감정 정보 조절적(긍정) 반응. 긍정-부정 vs 부정-긍정 비교: **p = 0.010**
- **개인차**: STAI-X1 불안 점수가 높을수록 1Emo 부정 조건에서 더 긍정적 방향의 인출 편향(positive bias). **p = 0.002, 0.003**

**의의**: 정서 맥락화 지각 디코딩의 뇌 네트워크 기반 확립. ACC 하위영역 분리는 Etkin et al. (2011) 이론 검증.

### 1.2 MixedEmo EEG (n=92, 32채널 scalp, 2048 Hz)

**설계**:
- 동일 피험자 코호트 (n=92)
- **32 채널 scalp EEG**, Sampling rate **2048 Hz**
- 전처리: 0.5–100 Hz bandpass, ICA, 1/f 변환

**바이오마커 (2종)**:
- **Posterior θ (두정엽·후두엽 theta)**: 감정 자극 제시 순간 감정 조건 > 중립 조건. 감정 정보 처리 우선시 마커.
- **Frontal θ (전두엽 theta)**: 혼합 조건(긍정-부정·부정-긍정) > 단일 조건. 감정 충돌 지각 마커.

**의의**: fMRI 공간 정보와 상보적인 EEG 시간·주파수 바이오마커 확립. 실시간 BCI 디코딩 토대.

### 1.3 해마 하위영역 OCAT (Object-Context Association Task)

**결과 (정확 인용)**: 좌측 해마 하위 영역인 **CA23DG와 CA1**에서 물체와 해당 물체가 연합 기억되었던 환경 간의 유의미한 패턴 유사성. 동일 환경 공유 물체들의 신경 표상이 서로 유사해지는 "**맥락 범주화 (contextual categorization)**".

### 1.4 가상공간 탐험 EEG — 랜드마크와 공간기억

**설계**:
- 참여자는 가상 공간 **1분 녹화 비디오** 수동 시청 후, 경로·도착지 관련 문제 수행
- 자극 공간: **4가지 랜드마크 유형** (근접, 원격, 혼합, 없음)
- EEG feature set: **6개 근접 채널기반 그룹 + 33개 주파수 기반 그룹**

**핵심 측정 — Sequential Reactivation**:
- 공간 탐험 event의 순차적 뇌 재활성을 **reactivation bias**로 측정
- reactivation bias = 0: 초반 event 강함, 종반 약함
- reactivation bias = 1: 종반 event 강함, 초반 약함
- **성공적 sequential reactivation = 시간에 따른 reactivation bias의 양의 상관**

**결과**:
- 디코딩 정확도 **10–15%** (chance-level 4%)
- 원거리 랜드마크 재활성화가 공간기억 성공과 유의 연관
- **출판**: Imaging Neuroscience 저널, **Lim et al., 2025년 8월 게재**

### 1.5 청소년 지각-공간 맥락 연합 발달 (만 9–18세)

**결과 (정확 인용)**: 지각-공간 맥락 연합 학습 중 해마 하위 영역 **CA23DG** 활성화. CA23DG ↔ **안와전두피질 (OFC)** 연결성 발달이 나이에 따른 지각-공간 맥락 연합 발달을 설명. **정서적 학대를 경험한 집단에서는 관찰되지 않음** — 환경적 요인의 신경발달 영향 입증.

### 1.6 의미 기반 맥락 계층화 (Semantic boundary)

**결과**: 물리적 시각 자극이 동일해도 맥락 변화만으로 **고위 시각영역 (lingual gyrus 등)** 활성 증가. 해마-시각영역-전전두피질 상호작용이 효율적 기억 구성 매개. 맥락 계층화 시 해마 개입 증대, 전전두 개입 감소.

### 1.7 공간 경계 지각 (spatial boundary)

**결과**: 물체-시공간 연합 학습 중 **subiculum** 및 해마 전체·CA23DG에서 경계 통과 직후 유의한 활성도 증가.

### 1.8 Plus-maze VR — 해마곁 영역 functional dissociation

**결과**: 참가자가 plus-maze 환경에서 사물-건물 연관 학습 후 fMRI 회상. **좌측 측후각피질 (perirhinal cortex, PrC)** — 강한 기억 수행은 공유 맥락에 따른 낮은 통합과 연관.

### 1.9 관련 논문 (제출본 17편 외 대표)

- Lim et al. 2025/8 *Imaging Neuroscience* (1.4 가상공간 탐험 EEG)
- Kim et al. 2025/11 *iScience*
- Lee et al. 2025/11 *Neuropsychologia*
- Koo et al. 2026/1 *Scientific Reports*

**정합성 노트**: 이 4편은 공식 achievements.yaml 17편 목록에 **미포함**. 사용자 결정: 제출본 그대로 유지.

---

## 2. 최형진 Lab — 동물 칼슘이미징·광유전학 (평가항목 #1 + 세부연구 5)

### 2.1 3D 골격 데이터베이스 — 자유 행동 설치류 멀티뷰

**설계**:
- **머리 고정 없이** 자유롭게 움직이는 개방형 행동 아레나
- **고해상도 적외선 카메라** 다각도 배치 (상·좌·우)
- **DeepLabCut** 기반 멀티뷰 3D 포즈 추정
- **골격 포인트**: 코·귀·목·척추(어깨·등·허리)·앞발·뒷발·꼬리 기저부·꼬리 끝

**자발 행동 라벨**: 그루밍(grooming), 보행(walking), 서기(rearing), drinking (positive valence)

**결과 (정확 인용)**:
- Baseline: 궤적이 아레나 전반 광범위 분포. **오른쪽 영역 (물 노즐 인접)** 히트맵 집중 — 물 보상 접근·탐색 행동
- **부정적 정서 상태**: 전 신체 부위 궤적 길이·히트맵 강도 전반 감소

**의의**: 자연스러운 환경 자극에서 동물의 행동·정서 상태를 정량화하는 기반. 정서 맥락화 지각 디코딩 DB의 동물 파트 확립.

### 2.2 VTA–NAc Two-site 광유전학-칼슘이미징 (세부연구 5, 평가항목 #3 선제)

**연구 질문**: 정서 가치 부여 핵심 회로인 VTA-NAc 도파민 축삭에 대한 인과적 개입은 지각·의사결정 편향을 어떻게 변화시키는가?

**방법 (정확 인용)**:
- **동물 모델**: DAT-cre 마우스
- **VTA 표적**: AAV5-Syn-FLEX-rc[ChrimsonR-tdTomato] 주입 → 594 nm 적색광 반응 흥분성 opsin 선택 발현
- **NAc 표적**: AAV9-hSyn-GRAB_DA1h 주입 → 세포외 도파민 농도 형광 센서
- **단일 광섬유 이식**: 동일 광섬유로 VTA-NAc 도파민 축삭 광자극 + GRAB_DA1h 형광 **fiber photometry** 동시 측정
- **자극 프로토콜**: 594 nm 레이저 · 30초 간 5/10/20 Hz 반복 자극 · NAc 도파민 신호 연속 기록

**결과**: VTA 도파민 뉴런 축삭 광자극 시 NAc GRAB_DA1h 형광이 자극 시작 직후 급격 상승.

**4차년도 확장 (정확 인용)**:
1. 특정 도파민 상태(저·중·고) 의도적 설정 후 감각 지각 및 의사결정 편향 비교
2. 자연발생 도파민 신호(보상 예측, valence 신호) 선택적 교란 → 정서 맥락화 지각의 인과적 기전 검증

### 2.3 편도체 개별신경 기반 정서 디코딩 (차지욱 Lab 공동, 2023.10–2025.02)

**협력**: 최형진·차지욱 공동. 참여학생: 김유빈, 서정우. 발표: 2024.01 iSRC 동계 성과보고회.

**연구 질문**: 편도체 individual neuron 앙상블 활동에서 정서 카테고리를 얼마나 뚜렷이 구별할 수 있는가? 어떤 subpopulation이 핵심인가?

**접근**:
- 설치류 **표정(facial expression) 데이터**로 정서 상태 정량화
- **개별 뉴런 앙상블 활동**을 정서 디코더 입력
- 모델이 분류에 활용한 주요 단서(특정 신경세포 집단 발화 패턴, 안구·입 주위 근육 움직임) 해석

**주요 발견** (정확 인용):
- "편도체는 특정 신경활동 패턴을 통해 공포를 구별한다"
- "입 움직임은 혐오 정서를 대표한다"
- 정서가 뇌의 neural code와 안면 표현 양식에 의해 표상되는 방식 규명
- 정서·인지·행동 상호작용 및 정서 이상 기반 정신·신경질환 기전 탐색 기반

### 2.4 확장 회로 연구 (BK21 자체평가 기반)

**CeA-Glp1R 뉴런 — GLP-1 혐오감 기전** (2025.08 KSBNS):
- 실시간 칼슘 이미징: Exendin-4 투여 시 CeA-Glp1R 활성이 LiCl (혐오 약물) 유사 수준으로 증가
- **맛있는 음식 후 활성 감소 / 맛없는 음식 후 활성 증폭** — 특이 반응 패턴
- 광유전학적 활성화 → GLP-1 약물과 동일한 섭식 감소 / 억제 → 혐오 반응 소실
- **Negative valence encoding의 직접 인과 증명**

**NAc-NPY 뉴런 — 기호성 음식 보상 학습** (SAMSUNG Humantech Paper Awards):
- 측좌핵 NPY 뉴런이 도파민으로 활성화
- 기호성 음식·연관 단서에 선택 반응
- 반복 긍정 경험 축적 → 과식 촉진 · 보상 기억 형성·유지에 필요·충분

**LH CaMKIIα+ 뉴런 이질성** (2025.08 KSBNS):
- 단일세포 RNA-seq + MERFISH로 Vglut2+/Vgat+/비전형 아형 발견
- 생체 내 fiber photometry + miniscope: 식욕 단계 순차 활성 → 음식 접촉 시 억제
- LH CaMKIIα+ Vgat+ 뉴런은 보상 신호 무반응 · 식욕 단계 전용

**AgRP → 척수 콜린성 → 근육 회로** (2024-2025):
- 시상하부 ARC의 AgRP 신경이 **척수 아세틸콜린 콜린성 뉴런과 직접 연결**
- chemogenetics (NAD+ 지속 활성화 바이러스)로 AgRP 활성 조절 → 운동 능력 변화 인과 입증
- 노화 → 신경 연결 감소 → 운동 저하

**주요 출판**:
- *Nature Biomedical Engineering* (2024.11, IF 26.3) — 무선·배터리 없는 영장류 신경 기록기, 32채널 유연 전극, 1개월+ 자유 이동 원숭이 기록
- *Science Advances* (2024.11, IF 12.5) — AgRP=need, LH LepR=motivation 분리 규범 프레임워크
- *Experimental & Molecular Medicine* (2025.05, IF 12.9) — LH 뉴런 4개 영역 분류 리뷰

---

## 3. 차지욱 Lab — fMRI·EEG·iEEG 파운데이션 모델 + 임상 응용 (평가항목 #2 + #4) ★ 슬라이드 2장

### 3.1 fMRI Foundation Models (슬라이드 S7A 원천)

#### 3.1.1 SwiFT — 8.8B parameter fMRI Foundation Model

**스케일**:
- **모델 크기**: 37M → 118M → 1.2B → **최대 88억 (8.8B) 파라미터**
- **사전학습 데이터**: UK Biobank + Human Connectome Project (HCP) + Adolescent Brain Cognitive Development (ABCD) — **총 5만 명 resting-state fMRI**
- **기법**: 최대 업데이트 파라미터화 (**Maximal update Parameterization, muP**) — 일관된 스케일링

**결과**:
- **Power-law 스케일링** 확인 (뇌영상 첫 대규모 사전학습 스케일링 법칙)
- **7.6% 성별 분류 정확도 향상** (HCP)
- SOTA 경쟁 모델 **BrainLM, Brain-JEPA** 상회
- Adaptability: 알츠하이머병 전환 예측 · 통증 상태 분류 · 항우울제 치료 반응 예측에서 SOTA

#### 3.1.2 SwiFT-IO — Sequence-to-Sequence 정서 디코딩 (R² = 0.96)

**아키텍처**: SwiFT + **Perceiver IO 인코더** → Sequence-to-Sequence 확장

**학습 데이터**: HBN (Healthy Brain Network) movie fMRI, **677명 × 12분**

**벤치마크** (제출본 원표):

| Model | Test MSE | Test MAE | Test R² |
|---|---|---|---|
| SVR (ROI-based) | 2.074 | 0.753 | -0.114 |
| SVR (PCA-based) | 2.093 | 0.778 | -0.125 |
| LSTM | 2.628 | 0.838 | -0.135 |
| **SwiFT-IO** | **0.125** | **0.137** | **0.960** |

**발표**: CCN 2025

#### 3.1.3 MBBN — Frequency-Specific Multi-Band fMRI

**핵심**: fMRI 신호를 **주파수 대역 분리** 후 disentangle 인코딩

**ADHD 발견 (정확 인용)**:
- **고주파 대역**: 실행기능·감각 통합·의사결정 연결성 장애
- **저주파 대역**: 운동 지각·사회 인지·시각 처리 변화
- **초저주파 대역**: 내장감각·항상성 조절 연결성 차이

**ASD**: 고주파 대역 언어·주의·작업기억·사회 인지 변화

**출판**: *Communications Biology* 리비전 (2026.1 출판 예정)

#### 3.1.4 NeuroMamba — State-Space fMRI Foundation

**기법**:
- **Mamba2 모델** 기반 가변 길이 처리
- 배경 제거로 **FLOPs 46.5% 절감**
- **NeRF (Neural Radiance Fields) 스타일 주파수 기반 위치 인코딩**

**결과**: **HCP 성별 분류 94.9%** — SwiFT (92.9%), NeuroSTORM (93.3%) 상회

#### 3.1.5 TabLeT — 2D DCAE fMRI 토크나이징 (CVPR 심사 중)

**기법**: 자연 이미지로 학습된 **2D DCAE (Deep Compression Autoencoder)** → fMRI 3D 볼륨을 **프레임당 27개 연속 토큰으로 압축**

**데이터**: UK Biobank 8,178명 + HCP 1,061명 + ADHD-200 533명

**투고**: CVPR 2026 심사 중

#### 3.1.6 잠재 확산 모델 (Latent Diffusion Transformer) — 4D fMRI 생성

**기법**: 3D VQ-GAN으로 fMRI 고차원 → 저차원 압축, 잠재공간 Latent Diffusion Transformer

**데이터**: HCP task fMRI

**성과**: 세계 최초 입력 조건 기반 4차원 시공간 뇌영상 생성

### 3.2 EEG/iEEG Foundation + 동물 칼슘 + 임상·생성 (슬라이드 S7B 원천)

#### 3.2.1 DIVER-1 — EEG/iEEG Foundation Model

**데이터 규모 (ephys FM 슬라이드 + 제출본)**:
- **5.3k 시간 iEEG + 54k 시간 EEG** 코퍼스
- **17.7k명 이상 피험자**, **1.6M 채널-시간**
- DIVER-2 로드맵: **50,000 시간 iEEG로 확장** (10× 스케일업)
- 비교: 이전 SOTA 5,000 시간 iEEG — DIVER-2는 **10배**

**혁신 아키텍처**:
- **Any-Variate Attention**
- **Sliding Temporal Conditional Positional Encoding (STCPE)**
- **Multi-Domain Reconstruction Objective** (원시 시계열 + FFT 계수 + STFT 스펙트로그램)

**Scaling Law — First Quantified for Ephys**:
- **Data-constrained Scaling Law** 준수
- 제한된 컴퓨팅 예산 내에서 **모델 크기보다 training epochs 우선**이 효율적
- LLM Kaplan Scaling Law (2020) 대응 — ephys 최초 정량적 스케일링 법칙

**컴퓨팅**:
- DIVER-1 사용 **1e20 FLOPs** = GPT-1의 **2배**, 이전 SOTA ephys 의 **77배**

**SOTA 달성**:
- **iEEG**: Neuroprobe 벤치마크 15개 청각·시각·언어 디코딩 과제. **13M 파라미터 DIVER-1**이 **BrainBERT (43M), PopT (63M)** 대형 모델 동등·상회
- **EEG**: FACED (감정 인식), PhysioNet-MI (운동 상상), MentalArithmetic (인지 부하)

**3-Phase 학습 전략**:
- **Phase 1 Foundation** (Pre-Training): unlabeled neural data at scale → universal representation
- **Phase 2 Alignment** (Post-Training, DIVER-Video): paired iEEG-Video 100 subjects 24/7 → Trimodal Alignment (low-level motor semantics ↔ behavior/intention/interaction)
- **Phase 3 Personalization**: 실시간 feedback → per-user/session 강건 closed-loop

**협력 PI**: Jiook Cha · Jay-Yoon Lee · Chun Kee Chung · Uri Hasson · Shinjae Yoo

**투고**: ICLR 2026 심사 중

#### 3.2.2 POYO-SSL — 동물 칼슘이미징 Cell-Pattern-Aware SSL

**문제 설정**: 신경 집단 내 이질성 (안정 세포 + 무작위 세포 혼재)으로 기존 SSL 데이터 스케일링 실패.

**혁신**: 이질성을 **역이용**하는 SSL 프레임워크

**데이터**: **Allen Brain Observatory** 칼슘 이미징. **SST, VIP, PVALB, NTSR1** 뉴런 대상 "예측 가능한 뉴런" 분류 (왜도·첨도 기준).

**아키텍처**: POYO+ 기반 Transformer 인코더 + **Skip-Connection U-Net 디코더** (시각 자극 재구성)

**결과**:
- From-scratch 대비 **+12~13% 상대 성능 향상**
- 영화 프레임 복원 **SSIM = 0.593**
- 방향 분류 (Drifting Gratings) **정확도 55.5%** (baseline 49.2%)
- **1.98배 데이터 효율성**

**투고**: ICLR 2026 리뷰 중, 2026.4 출판 예정

#### 3.2.3 Language-Brain Alignment — 의미 정렬 (+14.4%)

**성과**: Antonello et al. (기존 최고 모델) 대비 **+14.4%**

**혁신**:
- **RED (Relative Error Difference)** 상관계수 + Clustering
- **Convergence-Divergence-Zone Theory** 뇌과학 이론 정량 부합

**투고**: ICLR 2026 심사 중 (openreview.net/forum?id=hgBVVAJ1ym)

#### 3.2.4 CEBRA 기반 경외(Awe) 디코딩 — 세부연구 12-1

**VR 360도 영상 자극** + 뇌파 + 실시간 정서 반응

**혁신 지표**: **Cortical Distinctiveness**

**출판**: *Communications Psychology* (Lee et al., 2025)

#### 3.2.5 내수용감각 디코딩 ECG-EEG — 세부연구 12-2

**모달리티**: EEG + ECG + 연속적 감정 보고 + 자유 회상

**기법**:
- **CEBRA** 대조 학습
- **IS-RSA** 피험자 간 유사도
- **LLM 언어 분석** (Claude 3.5 Sonnet) 부정 편향 측정

#### 3.2.6 RYM (Revisit Your Memory) — EEG 기반 시청각 생성

**참가자**: 9명 (2세션, 3일 간격)

**파이프라인**:
- **Affect Extractor** (대조학습)
- **LLM**: Claude 3.5 Sonnet
- **Stable Diffusion** (시각 생성)
- **MusicGen** (음악 생성)

**결과**:
- **개인별 정서 디코딩 F1 Score = 0.9**
- **r = 0.265, p < 0.012** 상관
- **56% 선호도 향상** 대비 baseline

#### 3.2.7 Polygenic-informed Clinical Prediction

**관련 논문 (achievements.yaml)**:
- #1 "Polygenic scores for psychiatric traits mediate the impact of multigenerational history for depression on offspring psychopathology"
- #5 "Polygenic Risk-Informed White Matter Integrity Improves Deep Learning-Based Prediction of Youth Depression"
- #14 "Individual differences in effects of stressful life events on childhood ADHD: genetic, neural, familial contributions"
- #15 "Polygenic architecture of brain structure and function, behaviors, and psychopathologies in children"

**공통 기법**: genetic prior + deep learning → 정신건강 임상 예측 (우울증, ADHD)

#### 3.2.8 sMRI + Tabular 통합 (MCI→AD 조기진단)

**데이터**: ADNI 681명 MCI

**그룹화**: sMCI <75세, sMCI ≥75세, pMCI <75세, pMCI ≥75세

**기법**: Adaptive linear modulation (MMSE · CDR-SB · ADAS11 · FAQ · 교육 수준 · 성별 동시 조건화)

**평가**: GBA, WGA, NACC 일반화성

**투고**: *Biomedical Signal Processing and Control* 리뷰 중

### 3.3 차지욱 Lab Phase 전략 요약 (ephys FM 슬라이드)

- **Massive Compute**: 슈퍼컴퓨터 접근·전문성 (SNU+BNL Shinjae Yoo 협력)
- **Irreplaceable Data Moat**: 100+ 피험자 × 24/7 iEEG-Video-Speech 기록 접근
- **Test-Time Scaling** (Long Thinking) · Post-Training Scaling · Pre-Training Scaling 3축
- **DIVER-2 로드맵**: 50,000 시간 iEEG → BCI 스케일링 혁명 추진

---

## 4. 문태섭 Lab — Vision-Language + SEED + Quantum ML (평가항목 #5)

### 4.1 Vision-Language Model (VLM) — 뇌영상-언어 semantic 정렬

**목표**: 자연 이미지로 사전 학습된 대규모 VLM을 뇌영상 도메인에 전이학습 → UKB·ABCD·HCP 등 대규모 코호트의 다중 모달리티(sMRI·DTI·rsfMRI) 뇌영상 특징을 언어 모델 임베딩 공간에 투영

**실험 1 — CLIP-ViT 검증** (성별 분류 ACC, 제출본 원표):

| 데이터셋 | CNN | ViT | CLIP-ViT |
|---|---|---|---|
| ABCD (sMRI, n=11,316) | 0.92 | 0.805 | 0.802 |
| UKB (sMRI, n=42,794) | 0.98 | 0.93 | 0.94 |
| HCP (fMRI, n=1,200) | — | — | 0.81 |

**실험 2 — BLIP-2 vs LLaVA** (ABCD sMRI 성별):
- BLIP-2 = 0.779
- LLaVA = 0.787

**프롬프트 전략**: Simple QnA (LLaVA 0.787) > Chain-of-Thought (LLaVA 0.732)

**최종 선택**: LLaVA-Next-Interleave 아키텍처 (다중 영상 입력)

### 4.2 SEED — Semantic Evaluation for Visual Brain Decoding

**저자**: Juhyeon Park*, Peter Yongho Kim*, Jiook Cha, Shinjae Yoo, **Taesup Moon†** (교신)

**기관**: Seoul National University + Brookhaven National Lab

**문제 설정**: 기존 디코딩 평가 지표 (PixCorr · SSIM · AlexNet(2) · AlexNet(5) · Inception · CLIP · EfficientNet · SwAV) 가 perceptual detail·abstract feature에 편향 → 인간 판단과 불일치

**3개 제안 지표**:
1. **Object F1** — off-the-shelf object detector 기반 객체 존재 precision/recall (varying thresholds)
2. **Caption Similarity (Cap-Sim)** — 이미지 캡션 embedding 유사도 (caption = semantic bottleneck)
3. **SEED** — Object F1 + Cap-Sim + EffNet(feature-based) 3축 averaging · 상호 보완

**인간 판단 메타평가**:
- **22명 평가자 × 1,000 이미지쌍 = 22K 판단**
- 실제 뇌 디코딩 결과로 수행

**평가 대상 5개 SOTA 디코더**:
- MindEye2 (ICML 2024)
- NeuroPictor (ECCV 2024)
- UniBrain (arXiv 2024)
- MindBridge (CVPR 2024)
- BrainGuard (AAAI 2025)

**발견된 Failure Modes**:
- **Semantic Near-Miss Phenomenon** (예: Super-category 'animal' 안에서 dog ↔ bird 혼동)
- **Semantic Detail Confusion** (예: bird 정확하나 background가 ocean → 다른 semantic detail)

**활용**: MindEye2가 검색 기준 98%+ 정확도 보고하나 정성 평가에서 failure modes 드러남

**투고**: ICLR 2026

### 4.3 Quantum Time-series Transformer — rs-fMRI 분석

**구성 요소**:
- **Unitary Temporal Embedding** — 양자 임베딩
- **LCU (Linear Combination of Unitaries)** — 학습 가능 계수로 유니타리 연산을 양자 **중첩 (Superposition)** 상태로
- **QSVT (Quantum Singular Value Transformation)** — 비선형성 부여

**ADHD 응용 (정확 인용)**:
- **관련 뇌 네트워크**: 실행 제어 (Executive control) · 주의력 · 감정 조절 · 지각 (Perception) 네트워크 모두 ADHD 연관
- **복합적 원인 지지**: ADHD는 단순 전두엽 결함이 아닌, **뇌 여러 시스템의 복합 관여 (Multi-system involvement)**

**확장 계획**: Mamba · Hydra 기반 Quantum State Space Model

**관련 논문 (achievements.yaml)**: #12 "Resting-state fMRI Analysis using Quantum Time-series Transformer"

### 4.4 Quantum ML 확장 라인

- **#11 Quantum Mario**: Scalable Quantum RL with Multi-Chip Ensembles
- **#13 Over the Quantum Rainbow**: Explaining Hybrid Quantum RL

---

## 5. 4차년도 (2026) 계획과 Lab별 역할 분담

**예산**: 600,000천원 (직접비 468,750 + 간접비 131,250) · 약 6억원

**5개 핵심 방향** (공식 제출본 p89-91 인용):

### 방향 1 — 정서 맥락화 지각 DB 확장
- 동물 (최형진 Lab): 변동하는 자연 환경 자극 → 지각·정서 DB
- 사람 (이상아 Lab): 변동하는 자연 환경 자극 → 지각·정서 DB
- **BrainLife 공개**

### 방향 2 — ML 디코더 개발·검증
- 고정 환경·수동 경험: 동일종 다중 입력 분포 (차지욱 Lab SwiFT 계열)
- 가변 환경·능동 경험: 동일종 단일·다중 입력 분포

### 방향 3 — 신경과학 메커니즘 규명 (3년차 누락 항목, 4차년도 재개)
- **동물**: two-site 광유전학 + 칼슘이미징 → 감각-정서 직접 인과 (최형진·차지욱 공동 편도체 연구 확장)
- **사람**: 뇌전도·fMRI 단순/복합 자극 감각-정서 상호작용 및 개인차

### 방향 4 — 파운데이션 모델 전이학습 검증
- 동물: 대규모 행동·신경신호 → 사전학습 + 전이학습
- 사람: 대규모 다중 모달리티 (휴지기 / 과제 / 영화 / 자연자극 + EEG) → 사전학습 + 전이학습 (차지욱 Lab SwiFT·DIVER 확장)

### 방향 5 — 동물-사람 종간 파운데이션 통합
- 동물 신경·행동 + 사람 fMRI·EEG 통합 (4 Lab 교차 통합)
- 확장 가능성 검토

---

## 6. 기대효과 (4축, 제출본 p93-95)

### 1) 학문적
- UKB·ABCD급 데이터 공유로 뇌인지발달 연구 촉진
- 한국인 특이적 신경과학 지식
- 정서-지각 상호작용 인지신경과학 새 가설·증거
- "The Virtual Brain" 급 뇌 활동성 모델링

### 2) 의과학 기술
- 재현·일반화 가능 정신질환 바이오마커
- 비침습적 BCI 디코더
- **소아청소년 자살 예방** — 소아청소년은 판단·조절능력 부족, 심리 불안 요인 오인 가능

### 3) 교육
- 신경과학-초거대 AI 박사급 후속세대
- **인간형 AI**: 자주적 윤리·도덕·문화·심리·감정 요소

### 4) 사회·산업
- 마케팅: 소비자 craving/positive emotion 지수 측정, craving 지수 높은 디자인 선별, 엔터테인먼트 선호 예측

---

## 7. 평가항목 #3 누락 이슈 (평가단 질의 대비)

**원 평가기준표 (p12)**: 평가항목 3 "뇌-환경 상호작용 과정에서 정서에 의해 맥락화된 지각의 신경과학적 매커니즘 규명" — **가중치 10%** — 3차년도 목표 포함

**달성도 표 (p85) 실제**: 4개 항목 (#1/#2/#4/#5) × 25% 재분배 — **#3 누락**

**본문 실제 수행**:
- 세부연구 5 (동물 two-site VTA-NAc 광유전학) — **메커니즘 규명**
- 세부연구 6 (사람 EEG/fMRI 감각-정서) — 세부연구 12-1 (CEBRA 경외), 12-2 (내수용감각 ECG-EEG) 로 대체 기술
- 잠재 확산 모델, RYM, SEED도 이 섹션에 걸침

**해석**:
- 평가기준 재구성 — 평가항목 3이 "파운데이션 모델" 항목으로 대체, 가중치 10% → 25% 재분배
- 4차년도 계획에 **여전히 포함** (방향 3)
- 평가단 질의 시 구두 보완 필요

---

## 8. 핵심 지표 요약 (슬라이드 11 Hero 용)

- **합계 달성도**: 97.5%
- **공식 논문 실적**: 17편 + 학회 4건 = 21건
- **핵심 모델 수**: 5개 이상 멀티스케일 파운데이션 (SwiFT 8.8B · DIVER-1 · NeuroMamba · POYO-SSL · TabLeT)
- **4차년도 예산**: 600,000천원 (약 6억원)
- **데이터 규모**:
  - 동물 표정·음성 3,000건+
  - 인간 뇌영상 500명+
  - DIVER-1 코퍼스 5.3k iEEG + 54k EEG 시간
  - SwiFT 5만명 사전학습
