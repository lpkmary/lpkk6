import streamlit as st
st.title('Penyetaraan reaksi antara asam kuat dengan basa kuat')
tab1,tab2,tab3=st.tabs(['Informasi mengenai asam kuat','Informasi mengenai basa kuat','Penyetaraan reaksi'])

def cariHasilWithKurung(asamKuat, basaKuat):
    right_side = " + 2H2O"
    asam = asamKuat.split("H")[1]  # Br
    basa = basaKuat.split("(")[0]  # Ca
    number_of_basa = basaKuat.split(")")[1]
    left_side = f"{basa}({asam}){number_of_basa}"

    hasil = left_side + right_side
    temporary = f"2{asamKuat} + {basaKuat} → {hasil}"
    st.success(f"Hasil dari {asamKuat} + {basaKuat} -> {temporary}")

def cariHasil(asamKuat, basaKuat):
    isThereIsOinAsamKuat = 0
    if "O" in asamKuat:
        isThereIsOinAsamKuat = 1
    
    count_asam_kuat_h = asamKuat.count("H")
    count_asam_kuat_o = asamKuat.count("O") - isThereIsOinAsamKuat
    count_basa_kuat_h = basaKuat.count("H")
    count_basa_kuat_o = basaKuat.count("O")

    totalH = count_asam_kuat_h + count_basa_kuat_h
    totalO = count_asam_kuat_o + count_basa_kuat_o

    right_side = " + "
    h_side = "H"
    o_side = "O"
    if totalH > 1:
        h_side = f"H{totalH}"

    if totalO > 1:
        o_side = f"O{totalO}"

    right_side += f"{h_side}{o_side}"

with tab1:
    st.header('Informasi mengenai asam kuat', divider='rainbow')
    st.write('Asam kuat adalah asam yang dapat terionisasi sempurna di dalam air')
    st.write('beberapa contoh asam kuat adalah:')
    st.write('Asam klorida (HCL)')
    st.write('Asam nitrat (HNO3)')
    st.write('Asam sulfat (H2SO4)')
    st.write('Asam bromida (HBr)')
    st.write('Asam iodida (HI)')
    st.write('Asam klorat (HClO3)')
    st.write('Asam peklorat (HClO4)')

with tab2:
    st.header('Informasi mengenai basa kuat', divider='rainbow')
    st.write('Basa kuat adalah basa yang dapat terionisasi sempurna di dalam air')
    st.write('beberapa contoh basa kuat adalah:')
    st.write('Litium hidroksida (LiOH)')
    st.write('Natrium hidroksida (NaOH)')
    st.write('Kalium hidroksida (KOH)')
    st.write('Kalsium hidroksida (Ca(OH)2)')
    st.write('Rubidium hidroksida (RbOH)')
    st.write('Stronsium hidroksida (Sr(OH)2)')
    st.write('Sesium hidroksida (CsOH)')
    st.write('Barium hidroksida (Ba(OH)2)')
    st.write('Magnesium hidroksida (Mg(OH)2)')
    st.write('Berilium hidroksida (Be(OH)2)')

with tab3:
    st.header('Penyetaraan reaksi', divider='rainbow')
    st.write('Reaksi antara asam kuat dengan basa kuat akan menghasilkan pH larutan yang dihasilkan bersifat netral atau pH = 7')
    options1=st.selectbox(
        'pilih senyawa asam kuat',
        ['HCL','HNO3','H2SO4','HBr','HI','HClO3','HClO4'])
    
    options2=st.selectbox(
        'pilih senyawa basa kuat',
        ['LiOH', 'NaOH','KOH','Ca(OH)2','RbOH','Sr(OH)2','CsOH','Ba(OH)2','Mg(OH)2','Be(OH)2'])
    

    tombol=st.button('Penyetaraan reaksi')
    if tombol:
        hasil = cariHasil(options1, options2)