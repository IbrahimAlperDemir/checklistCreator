import streamlit as st
from generate_test_cases import generate_test_cases
from save_to_checklist import save_to_checklist
from form_tracker import get_next_form_number
import os

st.set_page_config(page_title="Test Case Checklist Oluşturucu", layout="wide")
st.title("🧪 Test Case (Checklist) Oluşturucu")

st.markdown("Lütfen aşağıdaki alanları doldurun:")

with st.form("testcase_form"):
    feature_name = st.text_input("1. Özellik Adı")
    test_purpose = st.text_area("2. Testin Amacı")
    test_type = st.selectbox("3. Test Tipi", ["Fonksiyonel", "Performans", "Güvenlik", "Uyumluluk", "Diğer"])
    preconditions = st.text_area("4. Ön Koşullar")
    steps = st.text_area("5. Test Adımları")
    expected = st.text_area("6. Beklenen Sonuç")

    submitted = st.form_submit_button("📄 Excel Oluştur")

if submitted:
    with st.spinner("Excel dosyası oluşturuluyor..."):
        inputs = {
            "feature_name": feature_name,
            "test_purpose": test_purpose,
            "test_type": test_type,
            "preconditions": preconditions,
            "steps": steps,
            "expected": expected
        }

        try:
            excel_text = generate_test_cases(inputs)
            revision = "A"
            doc_type = "TST"
            form_number = get_next_form_number(doc_type)
            filename = f"TestChecklist_{form_number}.xlsx"
            save_to_checklist(excel_text, filename, revision=revision)

            with open(filename, "rb") as f:
                st.success("✅ Excel dosyası hazır!")
                st.download_button(
                    label="📥 Excel İndir",
                    data=f,
                    file_name=filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except Exception as e:
            st.error(f"❌ Hata oluştu: {e}")
