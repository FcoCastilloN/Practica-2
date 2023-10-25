import heapq

# Funci�n para fusionar dos archivos ordenados
def merge_files(file1, file2, output_file):
                heapq.heappush(heap, (next_value, source_file))

# Funci�n para dividir un archivo en m�ltiples archivos m�s peque�os
def split_file(input_file, chunk_size):
    files = []
    
    with open(input_file) as input:
        buffer = []
        counter = 0
        for line in input:
            buffer.append(line)
            counter += 1
            if counter >= chunk_size:
                buffer.sort()  # Ordenar el b�fer en memoria
                with open(f'chunk_{len(files)}.txt', 'w') as output:
                    output.writelines(buffer)
                files.append(f'chunk_{len(files)}.txt')
                buffer = []
                counter = 0
        
        if buffer:
            buffer.sort()  # Ordenar el �ltimo b�fer en memoria
            with open(f'chunk_{len(files)}.txt', 'w') as output:
                output.writelines(buffer)
            files.append(f'chunk_{len(files)}.txt')
    
    return files

# Funci�n principal de ordenamiento polif�sico
def polyphase_sort(input_file, output_file):
    chunk_size = 1000  # Tama�o de cada b�fer
    num_chunks = 5  # N�mero de archivos a fusionar en cada paso
    
    # Dividir el archivo en b�feres m�s peque�os
    files = split_file(input_file, chunk_size)
    
    while len(files) > 1:
        next_files = []
        for i in range(0, len(files), num_chunks):
            chunk_files = files[i:i + num_chunks]
            output_chunk = f'output_{len(files)}.txt'
            merge_files(chunk_files[0], chunk_files[1], output_chunk)
            if len(chunk_files) > 2:
                for j in range(2, len(chunk_files)):
                    merge_files(output_chunk, chunk_files[j], output_chunk)
            next_files.append(output_chunk)
        files = next_files
    
    # Renombrar el archivo final
    import shutil
    shutil.move(files[0], output_file)

# Ejemplo de uso
input_file = 'unsorted_data.txt'
output_file = 'sorted_data.txt'
polyphase_sort(input_file, output_file)
