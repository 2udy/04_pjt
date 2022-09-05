# README

## url

##### movies/urls.py

```

```

## view

##### movies/views.py

```python
# 오답
movie.title = 'title
# 정답
movie.title = request.POST.get('title')
# 발생한 문제

# 보완점
```

## template

##### templates/new.html

```python
# 발생한 문제 : `genre`와 `movie.genre`가 같지 않다고 인식됨
# 오답
<option value=" {{ genre }} "> {{ genre }} </option>
# 해결방법 및 개념
value는 "" 안에 값을 string으로 저장한다.
{{genre}} 앞, 뒤에 있는 공백까지 함께 문자열로 저장 되었다.
# 정답
<option value="{{ genre }}"> {{ genre }} </option>

#발생한 문제 : score에 정수값만 입력됨
# 해결방법 및 개념
<input type="number">의 속성 step의 기본 값은 1 이다.
# 정답
<input type="number" step="0.01">
```

##### templates/edit.html

```python
# 발생한 문제: 
# 오답
{% if "{{genre}}" == "{{movie.genre}}" %}selected{% endif %}
# 정답
{% if genre == movie.genre %}selected{% endif %}
# 해결 방법 및 개념 정리
new.html 에서 value값을 잘못받았다.

```

##### templates/index.html

```python
# 발생한 문제
```
NoReverseMatch at /movies/
Reverse for 'detail' with no arguments not found. 1 pattern(s) tried: ['movies/(?P<pk>[0-9]+)/\\Z']
```
# 오답
<a href="{% url 'movies:detail' %}"> {{ movie.title }} </a>
# 해결 방법 및 개념 정리
'movies:detail'은  pk값 을 필요로 한다.
# 정답
<a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }} </a>
  
```


