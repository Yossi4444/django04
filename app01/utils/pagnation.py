"""
自定义的分页组件：以后要使用请按照如下步骤操作
    1、筛选需要的数据
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('id')
    2、实例化分页对象
    page_object = Pagination(request,queryset)
    context={
        'queryset': page_object.page_queryset,
        'page_string': page_object.html()
    }
    return render(request,'prettynum_list.html',context)
    3、在HTML页面中添加：
    # 循环query数据
    {% for item in queryset %}
        {{item.xx}}
    {% endfor %}
    # 分页条
    <form method="get">
      <nav aria-label="...">
      <ul class="pagination">
        {{page_string}}
      </ul>
      </nav>
    </form>
    4、要是想进行搜索功能：
    data_dict = {}
    value = request.GET.get('q', '')
    if value:
        # name__contains要变
        data_dict['name__contains'] = value
    # models.Admin.objects.filter中Admin要变
    queryset = models.Admin.objects.filter(**data_dict).order_by('id')
    # HTML网页中添加：
    <form method="get">
        <div style="float:right;width:250px" >
      <div class="input-group">
        <input type="text" class="form-control" placeholder="Search for..." name="q" value="{{value}}">
        <span class="input-group-btn">
          <button class="btn btn-default" type="submit">
            <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
          </button>
        </span>
      </div>
    </div>
      </form>
    # 最后在context中添加'value':value就可显示搜索的关键字
"""
from django.utils.safestring import mark_safe
class Pagination(object):
    def __init__(self,request,queryset,page_size=10,page_param='page',plus=4):
        """
        :param request:请求的对象
        :param queryset:符合条件的数据（根据这个数据进行分页处理）
        :param page_size:每页显示多少条数据
        :param page_param:在URL中传递的获取分页的参数（例如：http://127.0.0.1:8000/prettynum/list/?page=4）
        :param plus:显示当前页的前几和后几页
        """

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict=query_dict

        self.page_param = page_param
        page = request.GET.get(page_param,'1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset=queryset[self.start:self.end]

        total_count = queryset.count()
        # 总页面数
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

        self.plus = plus

    def html(self):
            start_page = self.page - self.plus
            end_page = self.page + self.plus + 1
            if start_page <= 0:
                start_page = 1
                end_page = 10
            if end_page > self.total_page_count + 1:
                end_page = self.total_page_count + 1
                start_page = self.total_page_count - 8
                if start_page < 1:
                    start_page = 1
            # 页码
            page_str_list = []

            self.query_dict.setlist(self.page_param, [1])
            # 首页
            page_first = '<li ><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(page_first)
            # 上一页
            if self.page > 1:
                self.query_dict.setlist(self.page_param, [self.page - 1])
                page_pre = '<li ><a href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
                    self.query_dict.urlencode())
            else:
                self.query_dict.setlist(self.page_param, [1])
                page_pre = '<li ><a href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
                    self.query_dict.urlencode())
            page_str_list.append(page_pre)
            for i in range(start_page, end_page):
                self.query_dict.setlist(self.page_param, [i])
                if i == self.page:
                    ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
                else:
                    ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
                page_str_list.append(ele)
            if self.page < self.total_page_count:
                self.query_dict.setlist(self.page_param, [self.page + 1])
                page_after = '<li><a href="?{}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'.format(
                    self.query_dict.urlencode())
            else:
                self.query_dict.setlist(self.page_param, [self.total_page_count])
                page_after = '<li><a href="?{}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'.format(
                    self.query_dict.urlencode())
            page_str_list.append(page_after)
            # 尾页
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            page_last = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(page_last)
            search_string = """
                <div class="input-group" style="width:100px;float:right">
                  <input type="text" class="form-control" name="page">
                  <span class="input-group-btn">
                    <button class="btn btn-default" type="submit">跳转</button>
                  </span>
                </div>
                """
            page_str_list.append(search_string)
            page_string = mark_safe("".join(page_str_list))
            return page_string
