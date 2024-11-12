def calculate_final_score(tugas, uts, uas):
    return (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)

def main():
    data_list = []
    
    while True:
        print("\nInput Data Mahasiswa")
        name = input("Nama: ")
        nim = input("NIM: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        
        final_score = calculate_final_score(tugas, uts, uas)
        data_list.append({
            'name': name,
            'nim': nim,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'final_score': final_score
        })
        
        more_data = input("Tambah data (y/t)? ").strip().lower()
        if more_data != 'y':
            break
    
    # Display data in table format
    print("\nDaftar Nilai Mahasiswa")
    print("=" * 50)
    print("| No | Nama      | NIM    | Tugas | UTS | UAS | Akhir |")
    print("=" * 50)
    
    for i, data in enumerate(data_list, start=1):
        print(f"| {i:2} | {data['name']:8} | {data['nim']:6} | {data['tugas']:5} | {data['uts']:3} | {data['uas']:3} | {data['final_score']:6.2f} |")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
