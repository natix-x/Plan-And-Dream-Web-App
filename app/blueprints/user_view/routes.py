from ...app.blueprints.lists import lists


@lists.route('/', defaults={'page': 'index'})
@lists.route('/<page>')
def main_view(page):
    return "HI LOOSERS"
