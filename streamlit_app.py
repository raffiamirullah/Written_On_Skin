%%writefile app.py
import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Skincare Brand App", page_icon="🧴", layout="wide")

st.title("🧴 Skincare Brand Management App")

# --- User Authentication (Placeholder) ---
def show_login_signup_page():
    st.sidebar.header("Login / Sign Up")
    choice = st.sidebar.radio("", ["Login", "Sign Up"])

    if choice == "Login":
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"): # In a real app, you'd check credentials here
            st.success("Logged in as {}".format(username))
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_rerun()

    elif choice == "Sign Up":
        st.sidebar.subheader("Create New Account")
        new_username = st.sidebar.text_input("New Username")
        new_password = st.sidebar.text_input("New Password", type="password")
        confirm_password = st.sidebar.text_input("Confirm Password", type="password")
        if new_password == confirm_password:
            if st.sidebar.button("Sign Up"): # In a real app, you'd save user data
                st.success("You have successfully created an account!")
                st.info("Go to Login Menu to login")
        else:
            st.sidebar.warning("Passwords do not match")


# --- Main Application Logic ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    show_login_signup_page()
else:
    st.sidebar.success(f"Welcome, {st.session_state['username']}!")
    if st.sidebar.button("Logout"): # Logout functionality
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.experimental_rerun()

    # --- Tabs for different functionalities ---
    tab1, tab2, tab3 = st.tabs(["Dashboard", "Pricing Tool", "Bookkeeping"])

    with tab1:
        st.header("Dashboard 📊")
        st.write("This is your main dashboard. We will add charts and summaries here.")
        # Placeholder for dashboard content

    with tab2:
        st.header("E-commerce Pricing Recommendation Tool 💰")
        st.write("Gunakan alat ini untuk menghitung keuntungan berdasarkan harga jual di e-commerce, setelah dipotong biaya admin.")

        st.subheader("Input Data Produk")
        product_cost = st.number_input("Modal Produk (Rp)", min_value=0.0, value=100000.0, step=1000.0)
        selling_price = st.number_input("Harga Jual di E-commerce (Rp)", min_value=0.0, value=150000.0, step=1000.0)

        st.subheader("Biaya E-commerce")
        platform = st.selectbox("Pilih Platform E-commerce", ["Shopee", "Tokopedia", "Lainnya"])

        if platform == "Shopee":
            commission_rate = st.slider("Persentase Komisi Shopee (%) (0-6%)", min_value=0.0, max_value=6.0, value=4.0, step=0.1)
            transaction_fee = st.slider("Biaya Transaksi Shopee (%) (0-3%)", min_value=0.0, max_value=3.0, value=2.0, step=0.1)
            # Example for Shopee: assume PPN for commission is also applicable
            ppn_commission_rate = st.slider("PPN atas Komisi (%) (0-11%)", min_value=0.0, max_value=11.0, value=11.0, step=0.1)
            # For simplicity, we are combining other potential fees. In a real scenario, you might break these down further.
            other_fees = st.number_input("Biaya Lain-lain (Rp) (Contoh: Subsidi Ongkir, Biaya Admin Penjual Lainnya)", min_value=0.0, value=5000.0, step=100.0)

        elif platform == "Tokopedia":
            commission_rate = st.slider("Persentase Komisi Tokopedia (%) (0-6%)", min_value=0.0, max_value=6.0, value=3.5, step=0.1)
            transaction_fee = st.slider("Biaya Transaksi Tokopedia (%) (0-3%)", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
            # For simplicity, we are combining other potential fees.
            other_fees = st.number_input("Biaya Lain-lain (Rp) (Contoh: Biaya Layanan, Biaya Promosi)", min_value=0.0, value=3000.0, step=100.0)
            ppn_commission_rate = 0.0 # Tokopedia might have different PPN application or already included

        else: # Lainnya
            commission_rate = st.slider("Persentase Komisi (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
            transaction_fee = st.slider("Biaya Transaksi (%)", min_value=0.0, max_value=5.0, value=1.5, step=0.1)
            ppn_commission_rate = st.slider("PPN atas Komisi (%) (0-11%)", min_value=0.0, max_value=11.0, value=11.0, step=0.1)
            other_fees = st.number_input("Biaya Lain-lain (Rp)", min_value=0.0, value=0.0, step=100.0)


        if st.button("Hitung Keuntungan"):
            # Calculate commission
            commission_amount = (commission_rate / 100) * selling_price
            
            # Calculate PPN on commission if applicable
            ppn_on_commission = (ppn_commission_rate / 100) * commission_amount

            # Calculate transaction fee
            transaction_fee_amount = (transaction_fee / 100) * selling_price

            # Total deductions
            total_deductions = commission_amount + ppn_on_commission + transaction_fee_amount + other_fees

            # Net Revenue
            net_revenue = selling_price - total_deductions

            # Gross Profit
            gross_profit = net_revenue - product_cost

            # Profit Margin
            if selling_price > 0:
                profit_margin = (gross_profit / selling_price) * 100
            else:
                profit_margin = 0.0

            st.subheader("Hasil Perhitungan")
            st.metric(label="Modal Produk", value=f"Rp {product_cost:,.2f}")
            st.metric(label="Harga Jual", value=f"Rp {selling_price:,.2f}")
            st.metric(label="Total Potongan E-commerce", value=f"Rp {total_deductions:,.2f}", delta=f"Komisi: Rp {commission_amount:,.2f}, PPN Komisi: Rp {ppn_on_commission:,.2f}, Transaksi: Rp {transaction_fee_amount:,.2f}, Lain-lain: Rp {other_fees:,.2f}")
            st.metric(label="Pendapatan Bersih", value=f"Rp {net_revenue:,.2f}")
            st.metric(label="Keuntungan Kotor", value=f"Rp {gross_profit:,.2f}", delta_color="off", help="Pendapatan Bersih - Modal Produk")
            st.metric(label="Margin Keuntungan", value=f"{profit_margin:,.2f} %", delta_color="off", help="(Keuntungan Kotor / Harga Jual) * 100%")

            if gross_profit < 0:
                st.warning("Anda mungkin mengalami kerugian dengan harga ini. Pertimbangkan untuk menyesuaikan harga atau mengurangi biaya.")
            elif profit_margin < 10:
                st.info("Margin keuntungan Anda rendah. Pertimbangkan strategi untuk meningkatkan keuntungan.")
            else:
                st.success("Keuntungan yang sehat! Jaga terus strategi Anda.")

    with tab3:
        st.header("Bookkeeping (Purchases & Sales) 📝")
        st.write("Record and track your purchases and sales here.")
        # Placeholder for bookkeeping content
