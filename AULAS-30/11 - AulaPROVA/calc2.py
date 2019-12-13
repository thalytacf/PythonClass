def calc_montante (capital, taxa_mesal, prazo):
    taxa = (1 + taxa_mesal)**prazo
    montante = capital * ((taxa)**prazo)
    taxa_anual = taxa - 1
    return montante, taxa_anual