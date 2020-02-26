# seasonl

Each season, clients purchase products on credit, and over the course of a season, they repay
their credit, and so clients have credit associated with them on a season-by-season basis. When a client makes a payment, we need to know which season the payment will be applied to,
as sometimes clients can have outstanding credit (debt) in more than one season. Since we still require that each saved repayment must
be associated with a season in our database, this offers greatuser experience in offering seasonless repayments where repayments are effected in a cascading fashion.
