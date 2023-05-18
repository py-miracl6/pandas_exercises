import streamlit as st
from streamlit_ace import st_ace
from pandas_func import *
import pandas as pd
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Pandas. Задача 5")

df = pd.read_csv("hr-analysis-prediction.csv")
data_check = pd.read_csv("hr-analysis-prediction.csv")
group_check = df.groupby(["Department", "EducationField", "Attrition"])[
    ["MonthlyIncome"]
].median()
group_check_2 = df.groupby(['Department', 'EducationField', 'Attrition']).MonthlyIncome.median().reset_index()

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        "- Вам дан датасет **hr-analysis-prediction.csv**\n"
        "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
        "- Создайте переменную **median_group**\n"
        "- Присвойте переменной **median_group** результат группировки датасета **df** по полям **Department, EducationField** и **Attrition**, в качестве функции агрегации выберите медиану по полю **MonthlyIncome** (должен быть тип DataFrame)"
    )
with col2:
    st.write("**Пример первых 5 строк результата:**")
    st.write(group_check[:5])


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
            assert data_check.equals(df), "Не перезаписывайте переменную df"
            # median_group
            assert (
                "median_group" in loc.keys()
            ), "Проверьте название переменной median_group"
            assert isinstance(
                loc["median_group"], pd.DataFrame
            ), "Проверьте тип переменной median_group, должен быть DataFrame"
            #st.dataframe(loc["median_group"])
            assert np.array_equal(
                loc["median_group"].index, group_check.index
            ) or np.array_equal(
                loc["median_group"].index, group_check_2.index
            ), "Проверьте признаки, по которым вы делали группировку"
            assert np.array_equal(
                loc["median_group"].columns, group_check.columns
            ) or np.array_equal(
                loc["median_group"].columns, group_check_2.columns
            ), "Проверьте признаки, по которым вы находили медиану"

            assert group_check.equals(
                loc["median_group"]
            ) or group_check_2.equals(
                loc["median_group"]
            ), "Проверьте результат в переменной median_group"

            st.success("Все верно! Ключ = 77")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
