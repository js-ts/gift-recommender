from flask import (
  Blueprint
)

bp = Blueprint('recommender_api', __name__)

@bp.route('/recommend/<int:num_recommendations>', methods=['GET'])
def recommend(num_recommendations):
  #likes = request.args.getlist('likes', type=int)
  #dislikes = request.args.getlist('dislikes', type=int)

  return {'product_ids': [x for x in range(num_recommendations)]}
