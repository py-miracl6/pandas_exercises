from streamlit_ace import st_ace
from pandas_func import *
import pandas as pd


hide_part_of_page()
st.subheader("HW9. Блок Pandas. Задача 1")

st.markdown(
    "- Вам дан датасет **hr-analysis-prediction.csv**\n"
    "- Импортируйте pandas и напишите краткий алиас **pd**\n"
    "- Прочитайте датасет hr-analysis-prediction.csv и запишите его в виде DataFrame в переменную **df**\n"
    "- Представьте, что датасет лежит в той же папке, что и ваш код."
)

data_check = pd.read_csv("hr-analysis-prediction.csv")

loc = {}
content = st_ace(
    placeholder="Ваш код",
    language="python",
    theme="chrome",
    keybinding="vscode",
    show_gutter=True,
    min_lines=10,
    key="ace",
)

if content:
    st.markdown("### Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        try:
            assert (
                "pd" in loc.keys()
            ), "Импортируйте pandas, а также используйте алиас pd"
            assert "df" in loc.keys(), "Проверьте название переменной df"
            assert isinstance(loc["df"], pd.DataFrame), "Проверьте тип переменной df"
            st.dataframe(loc["df"][:5])
            assert loc["df"].shape == data_check.shape, "Проверьте размер таблицы в  df"
            assert data_check.equals(loc["df"]), "Проверьте данные в df"
            st.success("Все верно! Ключ = 09")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
