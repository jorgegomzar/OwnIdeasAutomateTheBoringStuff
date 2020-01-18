import os

# The idea is to have it running every minute with crontab
# Modify the code to fit your needs

# ID: {tipo}-[asignatura-]nombrearchivo

SORTENER_FOLDER = '/home/jorge/Escritorio/SORTENER/'
UNI_PATH = '/home/jorge/Documentos/Universidad/Universidad/01-CURSO_2019-20/'
DISTRO_PATH = '/home/jorge/Documentos/Distros/'
FIRST_QUAT = 'Primer_Cuatrimestre/'
SECOND_QUAT = 'Segundo_Cuatrimestre/'
SUBJECTS_PATH = {
    FIRST_QUAT: {
        'TC': '01-TC/',
        'AM': '02-AM/',
        'DAD': '03-DAD/',
        'ARSS': '04-ARSS/',
        'CALCULO': '05-CALCULO/'
    },
    SECOND_QUAT: {

    }
}

# checks every file in the SORTENER_FOLDER
for root, dirs, files in os.walk(SORTENER_FOLDER):
    for filename in files:
        moved = False
        original_path = SORTENER_FOLDER + filename
        filename_array = filename.split('-')
        if (filename_array[0] == "UNI"):    # is it college material?
            subject, final_file_name = filename_array[1], filename_array[2]
            print(' [+] Buscando ' + subject + ' para ' + final_file_name)
            for k in SUBJECTS_PATH:
                for v in SUBJECTS_PATH[k]:
                    if v == subject:    # get right SUBJECT_PATH
                        final_path = UNI_PATH + k + SUBJECTS_PATH[k][v] + final_file_name
                        print(original_path + ' -> ' + final_path)
                        os.rename(original_path, final_path)    # move it
                        moved = True
        elif (filename_array[0] == "DISTRO"):   # is it a new distro?
            final_path = DISTRO_PATH + filename.lstrip("DISTRO-")
            print(original_path + ' -> ' + final_path)
            os.rename(original_path, final_path) # move it
            moved = True
        if not moved:
            print('Couldn\'t find the right path for file \"' + filename + '\". It was not moved.')
        else:
            print('File \"' + filename + '\" moved successfully')