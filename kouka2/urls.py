from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'kouka2'

# URLパターンを登録する変数
urlpatterns = [
    # kouka2アプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    # 写真投稿ページのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    # 投稿完了ページのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    # カテゴリ1一覧ページ
    # photos1/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategory1Viewに渡される
    path('photos1/<int:category1>',
         views.Category1View.as_view(),
         name = 'photos_cat1'
         ),
     # カテゴリ2一覧ページ
    # photos2/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategory2Viewに渡される
    path('photos2/<int:category2>',
         views.Category2View.as_view(),
         name = 'photos_cat2'
         ),
     # カテゴリ3一覧ページ
    # photos3/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategory3Viewに渡される
    path('photos3/<int:category3>',
         views.Category3View.as_view(),
         name = 'photos_cat3'
         ),

    # ユーザーの投稿一覧ページ
    # user-list/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてUserViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),

    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
         ),

    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてPhotoDeleteViewに渡される
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'
         ),

    # 属性ソートページ
    # element_sort/へのアクセスはElementViewを実行
    path('element_sort/', views.ElementSortView.as_view(), name = 'element_sort'),

    # マイページのカテゴリ1一覧ページ
    # my_photos1/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてMyCategory1Viewに渡される
    path('my_photos1/<int:category1>',
         views.MyCategory1View.as_view(),
         name = 'my_photos1'
         ),

     # マイページのカテゴリ2一覧ページ
    # my_photos2/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてMyCategory2Viewに渡される
    path('my_photos2/<int:category2>',
         views.MyCategory2View.as_view(),
         name = 'my_photos2'
         ),

     # マイページのカテゴリ3一覧ページ
    # my_photos3/<Categorysデーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてMyCategory3Viewに渡される
    path('my_photos3/<int:category3>',
         views.MyCategory3View.as_view(),
         name = 'my_photos3'
         ),

     
    # マイページの属性ソートページ
    # my_element_sort/へのアクセスはMyElementViewを実行
    path('my_element_sort/', views.MyElementSortView.as_view(), name = 'my_element_sort'),
     
    # 編集ページのアクセスはviewsモジュールのPhotoUpdateViewを実行
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo_update'),

    # 編集完了ページのアクセスはviewsモジュールのUpdateSuccessViewを実行
    path('update_done/',
         views.UpdateSuccessView.as_view(),
         name='update_done'),

    # 昇順ソートページ
    # old_sort/へのアクセスはOldSortViewを実行
    path('old_sort/', views.OldSortView.as_view(), name = 'old_sort'),

    # マイページの昇順ソートページ
    # my_old_sort/へのアクセスはMyOldSortViewを実行
    path('my_old_sort/', views.MyOldSortView.as_view(), name = 'my_old_sort'),

    # トップページの昇順検索ページ
    # searchへのアクセスはSearchViewを実行
    path('search/', views.SearchView.as_view(), name = 'search'),

     # マイページの昇順検索ページ
    # my_serach/へのアクセスはMySerachViewを実行
    path('my_search/', views.MySearchView.as_view(), name = 'my_search'),

]