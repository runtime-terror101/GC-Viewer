import streamlit as st
from Bio import SeqIO
from io import StringIO
from Bio.SeqUtils import gc_fraction
import pandas as pd

st.title("Problem 1: GC Viewer")
st.markdown("GC Viewer is a simple application to explore GC fractions of all sequences in a FASTA file")
st.markdown("Select a FASTA file to get started.")

st.header("Select a FASTA file")
uploaded_file = st.file_uploader("Select FASTA File", type="FASTA")

if uploaded_file:
	stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
	records = SeqIO.parse(stringio, "fasta")

	st.header("GC Fraction as Table")
	df = pd.DataFrame(columns=['GC Fraction'])
	df = df.rename_axis('Seq ID')
	for record in records:
		df.loc[record.id] = gc_fraction(record.seq)
	st.write(df)

	st.header("GC Fraction as Chart")
	st.bar_chart(data=df, y='GC Fraction')
