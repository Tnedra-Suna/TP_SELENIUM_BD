import os
from datetime import datetime
from pages.product_card import ProductCard


def generate_report(products: list[ProductCard], success: bool, errors: list[str] = None) -> str:
    lines = []
    lines.append("=" * 40)
    lines.append("=== RAPPORT TP4 ===")
    lines.append("=" * 40)
    lines.append(f"\nProduits trouvés : {len(products)}\n")

    for product in products:
        lines.append(f"  - {product.name} | {product.price}")

    lines.append("")

    if errors:
        lines.append("ERREURS DÉTECTÉES :")
        for err in errors:
            lines.append(f"  [!] {err}")
        lines.append("")

    if success:
        lines.append("TEST TERMINÉ AVEC SUCCÈS")
    else:
        lines.append("TEST ÉCHOUÉ")

    lines.append("=" * 40)
    report_text = "\n".join(lines)

    # Bonus 2 : export fichier texte
    os.makedirs("logs", exist_ok=True)
    report_filename = f"logs/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_text)

    return report_text