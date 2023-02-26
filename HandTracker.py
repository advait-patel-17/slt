import cv2
import mediapipe as mp
import math as math
from LetterCoordinates import getDatabase

def getletter(cap, success, image):
    min_index = -1
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    # For static images:
    # IMAGE_FILES = []
    # with mp_hands.Hands(
    #     static_image_mode=True,
    #     min_detection_confidence=0.5) as hands:
    #   for idx, file in enumerate(IMAGE_FILES):
    #     # Read an image, flip it around y-axis for correct handedness output (see
    #     # above).
    #     image = cv2.flip(cv2.imread(file), 1)
    #     # Convert the BGR image to RGB before processing.
    #     results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    #     # Print handedness and draw hand landmarks on the image.
    #     print('Handedness:', results.multi_handedness)
    #     if not results.multi_hand_landmarks:
    #       continue
    #     image_height, image_width, _ = image.shape
    #     annotated_image = image.copy()
    #     for hand_landmarks in results.multi_hand_landmarks:
    #       print('hand_landmarks:', hand_landmarks)
    #       print(
    #           f'Index finger tip coordinates: (',
    #           f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
    #           f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
    #       )
    #       mp_drawing.draw_landmarks(
    #           annotated_image,
    #           hand_landmarks,
    #           mp_hands.HAND_CONNECTIONS,
    #           mp_drawing_styles.get_default_hand_landmarks_style(),
    #           mp_drawing_styles.get_default_hand_connections_style())
    #     cv2.imwrite(
    #         '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
    #     # Draw hand world landmarks.
    #     if not results.multi_hand_world_landmarks:
    #       continue
    #     for hand_world_landmarks in results.multi_hand_world_landmarks:
    #       mp_drawing.plot_landmarks(
    #         hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

    # For webcam input:
    # cap = cv2.VideoCapture(0)


    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

    x_coords = [0.6929428577423096, 0.6510507464408875, 0.6401001214981079, 0.6910164952278137, 0.7367528080940247, 0.6647253632545471, 0.6478376388549805, 0.6429416537284851, 0.6399103999137878, 0.7110123038291931, 0.7100391387939453, 0.7094271183013916, 0.7047684788703918, 0.7510148286819458, 0.7696093916893005, 0.7710875272750854, 0.7661987543106079, 0.7850415110588074, 0.7989014983177185, 0.7811206579208374, 0.7607079148292542]

    y_coords = [0.9084469676017761, 0.8117717504501343, 0.6900393962860107, 0.5946272611618042, 0.5462969541549683, 0.5105783939361572, 0.3602712154388428, 0.2716399133205414, 0.18749475479125977, 0.5063217282295227, 0.3356495201587677, 0.2417580783367157, 0.15294301509857178, 0.5430518388748169, 0.39023086428642273, 0.30122098326683044, 0.21104872226715088, 0.6261026263237, 0.5031172633171082, 0.5356163382530212, 0.5969552397727966]

    z_coords = [4.6817651977448804e-09, -0.045929569751024246, -0.07056760042905807, -0.09465070813894272, -0.11761385947465897, -0.003050375496968627, -0.01805935986340046, -0.032584045082330704, -0.04688436910510063, -0.006616602651774883, -0.013177008368074894, -0.03225458040833473, -0.05225666984915733, -0.019713839516043663, -0.045705992728471756, -0.07910438627004623, -0.10315269231796265, -0.037543606013059616, -0.06306809186935425, -0.07782138139009476, -0.08918128162622452]

    # xV = [0.24281814694404602, 0.2884288430213928, 0.2983751893043518, 0.2522857189178467, 0.21016696095466614, 0.29356110095977783, 0.30981647968292236, 0.3192608952522278, 0.32220005989074707, 0.24337688088417053, 0.23272605240345, 0.22695021331310272, 0.21572943031787872, 0.20069943368434906, 0.1860840618610382, 0.2178046703338623, 0.23801091313362122, 0.16493107378482819, 0.1666790097951889, 0.19732621312141418, 0.21839873492717743]
    # xS = [0.2625739276409149, 0.30593445897102356, 0.32778671383857727, 0.299159437417984, 0.24958281219005585, 0.3238121569156647, 0.3185616731643677, 0.32036498188972473, 0.31257352232933044, 0.2737508714199066, 0.2722110152244568, 0.280312180519104, 0.2809719145298004, 0.2325010448694229, 0.22179074585437775, 0.24004489183425903, 0.24560265243053436, 0.19482532143592834, 0.1870037317276001, 0.20779111981391907, 0.2186979353427887]

    # yV = [0.8129962086677551, 0.7262125611305237, 0.5834144353866577, 0.4827764630317688, 0.4176093339920044, 0.4398258924484253, 0.29187676310539246, 0.19815126061439514, 0.11836335062980652, 0.4533212184906006, 0.28025487065315247, 0.17833569645881653, 0.09186312556266785, 0.50356125831604, 0.4340607523918152, 0.5349823832511902, 0.6020799875259399, 0.5787534117698669, 0.5275325179100037, 0.6018587946891785, 0.6569243669509888]
    # yS = [0.7809501886367798, 0.7108633518218994, 0.5915814638137817, 0.4868301451206207, 0.44413724541664124, 0.4586733877658844, 0.37999385595321655, 0.4609133005142212, 0.5055598020553589, 0.46003401279449463, 0.37364622950553894, 0.4784800708293915, 0.49941134452819824, 0.48565733432769775, 0.4034714698791504, 0.4940248131752014, 0.5339796543121338, 0.5346716642379761, 0.46791690587997437, 0.5219645500183105, 0.5559329986572266]

    # zV = [2.6607631653519093e-09, -0.02610173262655735, -0.0545877143740654, -0.0889400914311409, -0.12023445963859558, -0.015853991732001305, -0.053060587495565414, -0.08118734508752823, -0.10351800918579102, -0.03422455117106438, -0.08200480788946152, -0.11620679497718811, -0.13845917582511902, -0.05808081477880478, -0.10476928949356079, -0.10986775159835815, -0.10385706275701523, -0.08829376101493835, -0.12057987600564957, -0.1209481805562973, -0.11470860987901688]
    # zS = [-1.8258319856023775e-10, -0.03490692749619484, -0.053815022110939026, -0.07231586426496506, -0.08438490331172943, -0.008753631263971329, -0.022000635042786598, -0.0162931140512228, -0.012739473022520542, -0.01333459559828043, -0.03610794246196747, -0.03322397544980049, -0.022848492488265038, -0.025107108056545258, -0.051891013979911804, -0.0476873442530632, -0.034914467483758926, -0.04110994189977646, -0.051578328013420105, -0.046979956328868866, -0.038474757224321365]

    # allXs = []
    # allXs.append(xV)
    # allXs.append(xS)

    # allYs = []
    # allYs.append(yV)
    # allYs.append(yS)

    # allZs = []
    # allZs.append(zV)
    # allZs.append(zS)

    allXs, allYs, allZs = getDatabase()
    counter = 1
    stored_index = -1
    with mp_hands.Hands(
        max_num_hands=1,
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            # success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            # print(results.multi_hand_landmarks)
            # x, y, z = addToArray(results.multi_hand_landmarks)
            x = []
            y = []
            z = []
            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
                    for landMark in hand_landmarks.landmark:
                        x.append(landMark.x)
                        y.append(landMark.y)
                        z.append(landMark.z)
                    
                    # print(x)
                    # print(y)
                    # print(z)
                    # print("-------")
                    
                    if len(x) > 0:
                        min_error = 9132487.0
                        min_index = -1
                        for num in range(min(len(allXs), len(allYs), len(allZs))):
        #                    print(len(allXs))
        #                    print(num)
                            x_coords = allXs[num]
                            # print(x_coords[0])
                            y_coords = allYs[num]
                            z_coords = allZs[num]
                            deltaX = x[0] - x_coords[0]
                            deltaY = y[0] - y_coords[0]
                            deltaZ = z[0] - z_coords[0]

                            x_new = [i - deltaX for i in x]
                            y_new = [i - deltaY for i in y]
                            z_new = [i - deltaZ for i in z]
                            x_new = [x_new[i] - x_coords[i] for i in range(21)]
                            y_new = [y_new[i] - y_coords[i] for i in range(21)]
                            z_new = [z_new[i] - z_coords[i] for i in range(21)]
                            # print(x_new)
                            # print(y_new)
                            # print(z_new)
                            x_new = [i * i for i in x_new]
                            y_new = [i * i for i in y_new]
                            z_new = [i * i for i in z_new]
                            displacements = [math.sqrt(x_new[i] + y_new[i] + z_new[i]) for i in range(21)]
                            # print(sum(displacements))
                            # print(min_error)
                            if sum(displacements) < min_error:
                                min_error = sum(displacements)
                                min_index = num
                        # print(min_error)
                        # print(min_index)
                        # print(letters[min_index])
                        # if (min_index != stored_index):
                        #     stored_index = min_index
                        #     counter = 1
                        #     print(counter)
                        # elif (counter == 50):
                        #     message += letters[min_index]
                        #     counter = 0
                        # else:
                        #     counter += 1
                        #     print(counter)
                        # message += letters[min_index]
                # print("What's good Rahul")
            # print(len(results.multi_hand_landmarks))
            # print("ved")
            # if (message != "" and not results.multi_hand_landmarks):
            #     print(message)
            #     message = ""
            # Flip the image horizontally for a selfie-view display.
            # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            # if cv2.waitKey(5) & 0xFF == 27:
            #     break
            if min_index < 0: 
                return cv2.flip(image, 1), ' '
            return cv2.flip(image, 1), letters[min_index]
    cap.release()


    #i think using the small data set we do have, we can definitely explore reinforcement learning instead of generic neural net
    # if we can't find a data set....