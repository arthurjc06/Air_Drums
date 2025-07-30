print('Importando bibliotecas...', end=' ')
import cv2
import mediapipe as mp
import sound
import time
print('Concluído')

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=0)

# Processamento de frames
frame_counter = 0
process_every_n_frames = 2

# Guarda a última pose
last_pose_landmarks = None

# Guarda as coordenadas de cada parte
last_left_arm_y = None
last_right_arm_y = None
last_right_foot_y = None
last_left_foot_y = None

# Thresholds
arm_threshold = 0.02
foot_threshold = 0.02

# Guardar o último movimento
left_arm_up = True
right_arm_up = True
left_foot_up = True
right_foot_up = True

# Guarda o tempo da última batida
last_left_arm = 0
last_right_arm = 0
last_right_foot = 0
last_left_foot = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Não foi possível abrir o vídeo.")
    exit()
else:
    print("Carregando vídeo...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1

    scale = 0.5
    frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    frame = cv2.flip(frame, 1) # Mude esse valor caso a imagem apareça invertida
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame.flags.writeable = False

    if frame_counter % process_every_n_frames == 0:
        results = pose.process(frame)
        if results.pose_landmarks: last_pose_landmarks = results.pose_landmarks
        else: last_pose_landmarks = None

    frame.flags.writeable = True

    # Detecção de movimento
    if last_pose_landmarks:
        left_arm = last_pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_arm = last_pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_foot = last_pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        right_foot = last_pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]

        current_time = time.time()

        # Braço Esquerdo
        if last_left_arm_y is not None:

            y_change_left_arm = left_arm.y - last_left_arm_y

            if y_change_left_arm > arm_threshold: # Caso mova para baixo
                if left_arm_up: # Caso o último movimento tenha sido para cima
                    sound.play_drum(sound.hat)
                    last_left_arm = current_time
                left_arm_up = False
            elif y_change_left_arm < (-arm_threshold): # Caso mova para cima
                left_arm_up = True
            else: # Caso esteja parado
                pass # Mantém como está

        # Braço Direito
        if last_right_arm_y is not None:

            y_change_right_arm = right_arm.y - last_right_arm_y

            if y_change_right_arm > arm_threshold:  # Movimento para baixo
                if right_arm_up:
                    sound.play_drum(sound.snare)
                    last_right_arm = current_time
                right_arm_up = False
            elif y_change_right_arm < (-arm_threshold):  # Movimento para cima
                right_arm_up = True
            else:  # Parado
                pass

        # Perna Direita
        if last_right_foot_y is not None:

            y_change_right_foot = right_foot.y - last_right_foot_y

            if y_change_right_foot > foot_threshold:  # Movimento para baixo
                if right_foot_up:
                    sound.play_drum(sound.pedal)
                    last_right_foot = current_time
                right_foot_up = False
            elif y_change_right_foot < (-foot_threshold):  # Movimento para cima
                right_foot_up = True
            else:  # Parado
                pass

        # Perna Esquerda
        if last_left_foot_y is not None:

            y_change_left_foot = left_foot.y - last_left_foot_y

            if y_change_left_foot > foot_threshold:  # Movimento para baixo
                if left_foot_up:
                    sound.play_drum(sound.kick)
                    last_left_foot = current_time
                left_foot_up = False
            elif y_change_left_foot < (-foot_threshold):  # Movimento para cima
                left_foot_up = True
            else:  # Parado
                pass

        last_left_arm_y = left_arm.y
        last_right_arm_y = right_arm.y
        last_left_foot_y = left_foot.y
        last_right_foot_y = right_foot.y

    else:
        last_left_arm_y = None
        last_right_arm_y = None
        last_right_foot_y = None
        last_left_foot_y = None

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if last_pose_landmarks:
        mp_drawing.draw_landmarks(frame, last_pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Air Drums', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

sound.mixer.quit()
cap.release()
cv2.destroyAllWindows()
pose.close()
