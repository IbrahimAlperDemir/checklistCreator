import streamlit as st
from generate_test_cases import generate_test_cases
from save_to_checklist import save_to_checklist

st.title("🧪 Test Case / Checklist Oluşturucu")
st.markdown("Yeni bir özellik için test senaryolarınızı aşağıdan oluşturabilirsiniz.")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Testin Amacı")
    test_type = st.selectbox("3. Test Tipi", ["Fonksiyonel", "Performans", "Güvenlik", "Kullanılabilirlik", "Uyumluluk"])
    preconditions = st.text_area("4. Ön Koşullar")
    steps = st.text_area("5. Test Adımları")
    expected = st.text_area("6. Beklenen Sonuçlar")

    revision = st.text_input("Revizyon", value="A")
    submitted = st.form_submit_button("✅ Test Checklist Oluştur")

if submitted:
    with st.spinner("Test senaryoları oluşturuluyor..."):
        data = {
            "feature_name": feature_name,
            "test_purpose": test_purpose,
            "test_type": test_type,
            "preconditions": preconditions,
            "steps": steps,
            "expected": expected
        }
        output_text = generate_test_cases(data)
        filename = "Test_Case_Listesi.xlsx"
        save_to_checklist(output_text, filename, revision=revision)

        with open(filename, "rb") as file:
            st.success("✔️ Test checklist hazır!")
            st.download_button(
                label="📥 Excel olarak indir",
                data=file,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
