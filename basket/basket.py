
class Basket:
    """
    A base basket class, providing some default behaviours that
    can be inherited or override as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('s_key')
        if 's_key' not in request.sesson:
            basket = self.session['s_key'] = {}
        self.basket = basket
