bash bash_run/run_tf_gpt4_n_long.sh
bash bash_run/run_tf_gpt4_n_short.sh
bash bash_run/run_tf_text3_n_long.sh
bash bash_run/run_tf_text3_n_short.sh
bash bash_run/run_tf_turbo_n_long.sh
bash bash_run/run_tf_turbo_n_short.sh

bash bash_run/run_sess_gpt4_n_long.sh
bash bash_run/run_sess_gpt4_n_short.sh
bash bash_run/run_sess_text3_n_long.sh
bash bash_run/run_sess_text3_n_short.sh
bash bash_run/run_sess_turbo_n_long.sh
bash bash_run/run_sess_turbo_n_short.sh

python main.py --eval --dataset=long --tf --model=gpt4 --second 
python main.py --eval --dataset=short --tf --model=gpt4 --second
python main.py --eval --dataset=long --tf --model=text3 --second
python main.py --eval --dataset=short --tf --model=text3 --second
python main.py --eval --dataset=long --tf --model=turbo --second
python main.py --eval --dataset=short --tf --model=turbo --second

python main.py --eval --dataset=long --sess --model=gpt4 --second 
python main.py --eval --dataset=short --sess --model=gpt4 --second
python main.py --eval --dataset=long --sess --model=text3 --second
python main.py --eval --dataset=short --sess --model=text3 --second
python main.py --eval --dataset=long --sess --model=turbo --second
python main.py --eval --dataset=short --sess --model=turbo --second

bash bash_run/run_tf_gpt4_all_long.sh
bash bash_run/run_tf_gpt4_all_short.sh
bash bash_run/run_tf_text3_all_long.sh
bash bash_run/run_tf_text3_all_short.sh
bash bash_run/run_tf_turbo_all_long.sh
bash bash_run/run_tf_turbo_all_short.sh

python main.py --test --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection

python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15



python main.py --test --dataset=long --tf --model=gpt4 --api_update


bash bash_run/run_tf_gpt4_n_long_update.sh
bash bash_run/run_tf_gpt4_n_short_update.sh
bash bash_run/run_tf_text3_n_long_update.sh
bash bash_run/run_tf_text3_n_short_update.sh
bash bash_run/run_tf_turbo_n_long_update.sh
bash bash_run/run_tf_turbo_n_short_update.sh

bash bash_run/run_tf_gpt4_n_long_lack.sh
bash bash_run/run_tf_gpt4_n_short_lack.sh
bash bash_run/run_tf_text3_n_long_lack.sh
bash bash_run/run_tf_text3_n_short_lack.sh
bash bash_run/run_tf_turbo_n_long_lack.sh
bash bash_run/run_tf_turbo_n_short_lack.sh

python main.py --eval --dataset=long --tf --model=gpt4 --api_lack
python main.py --eval --dataset=short --tf --model=gpt4 --api_lack

python main.py --eval --dataset=long --tf --model=gpt4 --api_update --second
python main.py --eval --dataset=short --tf --model=gpt4 --api_update --second
python main.py --eval --dataset=long --tf --model=turbo --api_update --second
python main.py --eval --dataset=short --tf --model=turbo --api_update --second
python main.py --eval --dataset=long --tf --model=text3 --api_update --second
python main.py --eval --dataset=short --tf --model=text3 --api_update --second

bash bash_run/run_tf_gpt4_n_long_noisy.sh
bash bash_run/run_tf_gpt4_n_short_noisy.sh
bash bash_run/run_tf_text3_n_long_noisy.sh
bash bash_run/run_tf_text3_n_short_noisy.sh
bash bash_run/run_tf_turbo_n_long_noisy.sh
bash bash_run/run_tf_turbo_n_short_noisy.sh

bash bash_run/run_tf_gpt4_n_long_robust0.sh
bash bash_run/run_tf_gpt4_n_short_robust0.sh
bash bash_run/run_tf_text3_n_long_robust0.sh
bash bash_run/run_tf_text3_n_short_robust0.sh
bash bash_run/run_tf_turbo_n_long_robust0.sh
bash bash_run/run_tf_turbo_n_short_robust0.sh

bash bash_run/run_tf_gpt4_n_long_robust1.sh
bash bash_run/run_tf_gpt4_n_short_robust1.sh
bash bash_run/run_tf_text3_n_long_robust1.sh
bash bash_run/run_tf_text3_n_short_robust1.sh
bash bash_run/run_tf_turbo_n_long_robust1.sh
bash bash_run/run_tf_turbo_n_short_robust1.sh

bash bash_run/run_tf_gpt4_n_long_robust2.sh
bash bash_run/run_tf_gpt4_n_short_robust2.sh
bash bash_run/run_tf_text3_n_long_robust2.sh
bash bash_run/run_tf_text3_n_short_robust2.sh

running



bash bash_run/run_tf_turbo_n_long_robust2.sh
bash bash_run/run_tf_turbo_n_short_robust2.sh

bash bash_run/run_tf_gpt4_n_long_robust3.sh
bash bash_run/run_tf_gpt4_n_short_robust3.sh
bash bash_run/run_tf_text3_n_long_robust3.sh
bash bash_run/run_tf_text3_n_short_robust3.sh
bash bash_run/run_tf_turbo_n_long_robust3.sh
bash bash_run/run_tf_turbo_n_short_robust3.sh

python main.py --eval --dataset=long --tf --model=gpt4 --noisy
python main.py --eval --dataset=short --tf --model=gpt4 --noisy
python main.py --eval --dataset=long --tf --model=turbo --noisy
python main.py --eval --dataset=short --tf --model=turbo --noisy
python main.py --eval --dataset=long --tf --model=text3 --noisy
python main.py --eval --dataset=short --tf --model=text3 --noisy

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=0

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=1

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=2

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=3

python main.py --test --dataset=long --tf --model=turbo --robust --robust_num=2 --resume



bash bash_run/run_tf_gpt4_n_long_update.sh
bash bash_run/run_tf_gpt4_n_short_update.sh
bash bash_run/run_tf_text3_n_long_update.sh
bash bash_run/run_tf_text3_n_short_update.sh
bash bash_run/run_tf_turbo_n_long_update.sh
bash bash_run/run_tf_turbo_n_short_update.sh

bash bash_run/run_tf_gpt4_n_long_lack.sh
bash bash_run/run_tf_gpt4_n_short_lack.sh
bash bash_run/run_tf_text3_n_long_lack.sh
bash bash_run/run_tf_text3_n_short_lack.sh
bash bash_run/run_tf_turbo_n_long_lack.sh
bash bash_run/run_tf_turbo_n_short_lack.sh

bash bash_run/run_tf_gpt4_n_long_robust0.sh
bash bash_run/run_tf_gpt4_n_short_robust0.sh
bash bash_run/run_tf_text3_n_long_robust0.sh
bash bash_run/run_tf_text3_n_short_robust0.sh
bash bash_run/run_tf_turbo_n_long_robust0.sh
bash bash_run/run_tf_turbo_n_short_robust0.sh

bash bash_run/run_tf_gpt4_n_long_robust1.sh
bash bash_run/run_tf_gpt4_n_short_robust1.sh
bash bash_run/run_tf_text3_n_long_robust1.sh
bash bash_run/run_tf_text3_n_short_robust1.sh
bash bash_run/run_tf_turbo_n_long_robust1.sh
bash bash_run/run_tf_turbo_n_short_robust1.sh

bash bash_run/run_tf_gpt4_n_long_robust2.sh
bash bash_run/run_tf_gpt4_n_short_robust2.sh
bash bash_run/run_tf_text3_n_long_robust2.sh
bash bash_run/run_tf_text3_n_short_robust2.sh
bash bash_run/run_tf_turbo_n_long_robust2.sh
bash bash_run/run_tf_turbo_n_short_robust2.sh

bash bash_run/run_tf_gpt4_n_long_robust3.sh
bash bash_run/run_tf_gpt4_n_short_robust3.sh
bash bash_run/run_tf_text3_n_long_robust3.sh
bash bash_run/run_tf_text3_n_short_robust3.sh
bash bash_run/run_tf_turbo_n_long_robust3.sh
bash bash_run/run_tf_turbo_n_short_robust3.sh

bash bash_run/run_sess_gpt4_n_long_noisy.sh
bash bash_run/run_sess_gpt4_n_short_noisy.sh
bash bash_run/run_sess_text3_n_long_noisy.sh
bash bash_run/run_sess_text3_n_short_noisy.sh
bash bash_run/run_sess_turbo_n_long_noisy.sh
bash bash_run/run_sess_turbo_n_short_noisy.sh


# OKay!

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=0

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=1

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=2

python main.py --eval --dataset=long --tf --model=gpt4 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=gpt4 --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=turbo --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=turbo --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=text3 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=text3 --robust --robust_num=3

python main.py --eval --dataset=long --sess --model=gpt4 --noisy
python main.py --eval --dataset=short --sess --model=gpt4 --noisy
python main.py --eval --dataset=long --sess --model=turbo --noisy
python main.py --eval --dataset=short --sess --model=turbo --noisy
python main.py --eval --dataset=long --sess --model=text3 --noisy
python main.py --eval --dataset=short --sess --model=text3 --noisy

python main.py --eval --dataset=long --tf --model=gpt4 --api_update --second
python main.py --eval --dataset=short --tf --model=gpt4 --api_update --second
python main.py --eval --dataset=long --tf --model=turbo --api_update --second
python main.py --eval --dataset=short --tf --model=turbo --api_update --second
python main.py --eval --dataset=long --tf --model=text3 --api_update --second
python main.py --eval --dataset=short --tf --model=text3 --api_update --second

python main.py --eval --dataset=long --tf --model=gpt4 --api_lack
python main.py --eval --dataset=short --tf --model=gpt4 --api_lack
python main.py --eval --dataset=long --tf --model=turbo --api_lack
python main.py --eval --dataset=short --tf --model=turbo --api_lack
python main.py --eval --dataset=long --tf --model=text3 --api_lack
python main.py --eval --dataset=short --tf --model=text3 --api_lack





bash bash_run/run_sess_gpt4_n_long_update.sh
bash bash_run/run_sess_gpt4_n_short_update.sh
bash bash_run/run_sess_text3_n_long_update.sh
bash bash_run/run_sess_text3_n_short_update.sh
bash bash_run/run_sess_turbo_n_long_update.sh
bash bash_run/run_sess_turbo_n_short_update.sh

python main.py --eval --dataset=long --sess --model=gpt4 --api_update
python main.py --eval --dataset=short --sess --model=gpt4 --api_update
python main.py --eval --dataset=long --sess --model=turbo --api_update
python main.py --eval --dataset=short --sess --model=turbo --api_update
python main.py --eval --dataset=long --sess --model=text3 --api_update
python main.py --eval --dataset=short --sess --model=text3 --api_update

bash bash_run/run_sess_gpt4_n_long_lack.sh
bash bash_run/run_sess_gpt4_n_short_lack.sh
bash bash_run/run_sess_text3_n_long_lack.sh
bash bash_run/run_sess_text3_n_short_lack.sh
bash bash_run/run_sess_turbo_n_long_lack.sh
bash bash_run/run_sess_turbo_n_short_lack.sh

python main.py --eval --dataset=long --sess --model=gpt4 --api_lack
python main.py --eval --dataset=short --sess --model=gpt4 --api_lack
python main.py --eval --dataset=long --sess --model=turbo --api_lack
python main.py --eval --dataset=short --sess --model=turbo --api_lack
python main.py --eval --dataset=long --sess --model=text3 --api_lack
python main.py --eval --dataset=short --sess --model=text3 --api_lack

bash bash_run/run_sess_gpt4_n_long_robust0.sh
bash bash_run/run_sess_gpt4_n_short_robust0.sh
bash bash_run/run_sess_text3_n_long_robust0.sh
bash bash_run/run_sess_text3_n_short_robust0.sh
bash bash_run/run_sess_turbo_n_long_robust0.sh
bash bash_run/run_sess_turbo_n_short_robust0.sh

python main.py --eval --dataset=long --sess --model=gpt4 --robust --robust_num=0

python main.py --eval --dataset=short --sess --model=gpt4 --robust --robust_num=0 *****

python main.py --eval --dataset=long --sess --model=turbo --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=turbo --robust --robust_num=0
python main.py --eval --dataset=long --sess --model=text3 --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=text3 --robust --robust_num=0

bash bash_run/run_sess_gpt4_n_long_robust1.sh
bash bash_run/run_sess_gpt4_n_short_robust1.sh
bash bash_run/run_sess_text3_n_long_robust1.sh
bash bash_run/run_sess_text3_n_short_robust1.sh
bash bash_run/run_sess_turbo_n_long_robust1.sh
bash bash_run/run_sess_turbo_n_short_robust1.sh

python main.py --eval --dataset=long --sess --model=gpt4 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=gpt4 --robust --robust_num=1 
python main.py --eval --dataset=long --sess --model=turbo --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=turbo --robust --robust_num=1
python main.py --eval --dataset=long --sess --model=text3 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=text3 --robust --robust_num=1

bash bash_run/run_sess_gpt4_n_long_robust2.sh
bash bash_run/run_sess_gpt4_n_short_robust2.sh
bash bash_run/run_sess_text3_n_long_robust2.sh
bash bash_run/run_sess_text3_n_short_robust2.sh
bash bash_run/run_sess_turbo_n_long_robust2.sh
bash bash_run/run_sess_turbo_n_short_robust2.sh

python main.py --eval --dataset=long --sess --model=gpt4 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=gpt4 --robust --robust_num=2 
python main.py --eval --dataset=long --sess --model=turbo --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=turbo --robust --robust_num=2
python main.py --eval --dataset=long --sess --model=text3 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=text3 --robust --robust_num=2

bash bash_run/run_sess_gpt4_n_long_robust3.sh
bash bash_run/run_sess_gpt4_n_short_robust3.sh
bash bash_run/run_sess_text3_n_long_robust3.sh
bash bash_run/run_sess_text3_n_short_robust3.sh
bash bash_run/run_sess_turbo_n_long_robust3.sh
bash bash_run/run_sess_turbo_n_short_robust3.sh

python main.py --eval --dataset=long --sess --model=gpt4 --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=gpt4 --robust --robust_num=3 
python main.py --eval --dataset=long --sess --model=turbo --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=turbo --robust --robust_num=3
python main.py --eval --dataset=long --sess --model=text3 --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=text3 --robust --robust_num=3







bash bash_run/run_sess_gpt4_all_long.sh
bash bash_run/run_sess_gpt4_all_short.sh
bash bash_run/run_sess_text3_all_long.sh
bash bash_run/run_sess_text3_all_short.sh
bash bash_run/run_sess_turbo_all_long.sh
bash bash_run/run_sess_turbo_all_short.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15

bash bash_run/run_sess_gpt4_all_long_noisy.sh
bash bash_run/run_sess_gpt4_all_short_noisy.sh
bash bash_run/run_sess_text3_all_long_noisy.sh
bash bash_run/run_sess_text3_all_short_noisy.sh
bash bash_run/run_sess_turbo_all_long_noisy.sh
bash bash_run/run_sess_turbo_all_short_noisy.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --noisy

bash bash_run/run_sess_gpt4_all_long_update.sh
bash bash_run/run_sess_gpt4_all_short_update.sh
bash bash_run/run_sess_text3_all_long_update.sh
bash bash_run/run_sess_text3_all_short_update.sh
bash bash_run/run_sess_turbo_all_long_update.sh
bash bash_run/run_sess_turbo_all_short_update.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update

bash bash_run/run_sess_gpt4_all_long_robust0.sh
bash bash_run/run_sess_gpt4_all_short_robust0.sh
bash bash_run/run_sess_text3_all_long_robust0.sh
bash bash_run/run_sess_text3_all_short_robust0.sh
bash bash_run/run_sess_turbo_all_long_robust0.sh
bash bash_run/run_sess_turbo_all_short_robust0.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0

bash bash_run/run_sess_gpt4_all_long_robust1.sh
bash bash_run/run_sess_gpt4_all_short_robust1.sh
bash bash_run/run_sess_text3_all_long_robust1.sh
bash bash_run/run_sess_text3_all_short_robust1.sh
bash bash_run/run_sess_turbo_all_long_robust1.sh
bash bash_run/run_sess_turbo_all_short_robust1.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1

bash bash_run/run_sess_gpt4_all_long_robust2.sh
bash bash_run/run_sess_gpt4_all_short_robust2.sh
bash bash_run/run_sess_text3_all_long_robust2.sh
bash bash_run/run_sess_text3_all_short_robust2.sh
bash bash_run/run_sess_turbo_all_long_robust2.sh
bash bash_run/run_sess_turbo_all_short_robust2.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2

bash bash_run/run_sess_gpt4_all_long_robust3.sh
bash bash_run/run_sess_gpt4_all_short_robust3.sh
bash bash_run/run_sess_text3_all_long_robust3.sh
bash bash_run/run_sess_text3_all_short_robust3.sh
bash bash_run/run_sess_turbo_all_long_robust3.sh
bash bash_run/run_sess_turbo_all_short_robust3.sh
python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3




bash bash_run/run_tf_gpt4_all_long.sh
bash bash_run/run_tf_gpt4_all_short.sh
bash bash_run/run_tf_text3_all_long.sh
bash bash_run/run_tf_text3_all_short.sh
bash bash_run/run_tf_turbo_all_long.sh
bash bash_run/run_tf_turbo_all_short.sh

bash bash_run/run_tf_gpt4_all_long_lack.sh
bash bash_run/run_tf_gpt4_all_short_lack.sh
bash bash_run/run_tf_text3_all_long_lack.sh
bash bash_run/run_tf_text3_all_short_lack.sh
bash bash_run/run_tf_turbo_all_long_lack.sh
bash bash_run/run_tf_turbo_all_short_lack.sh

bash bash_run/run_tf_gpt4_all_long_update.sh
bash bash_run/run_tf_gpt4_all_short_update.sh
bash bash_run/run_tf_text3_all_long_update.sh
bash bash_run/run_tf_text3_all_short_update.sh
bash bash_run/run_tf_turbo_all_long_update.sh
bash bash_run/run_tf_turbo_all_short_update.sh

bash bash_run/run_tf_gpt4_all_long_noisy.sh
bash bash_run/run_tf_gpt4_all_short_noisy.sh
bash bash_run/run_tf_text3_all_long_noisy.sh
bash bash_run/run_tf_text3_all_short_noisy.sh
bash bash_run/run_tf_turbo_all_long_noisy.sh
bash bash_run/run_tf_turbo_all_short_noisy.sh

bash bash_run/run_tf_gpt4_all_long_robust0.sh
bash bash_run/run_tf_gpt4_all_short_robust0.sh
bash bash_run/run_tf_text3_all_long_robust0.sh
bash bash_run/run_tf_text3_all_short_robust0.sh
bash bash_run/run_tf_turbo_all_long_robust0.sh
bash bash_run/run_tf_turbo_all_short_robust0.sh

bash bash_run/run_tf_gpt4_all_long_robust1.sh
bash bash_run/run_tf_gpt4_all_short_robust1.sh
bash bash_run/run_tf_text3_all_long_robust1.sh
bash bash_run/run_tf_text3_all_short_robust1.sh
bash bash_run/run_tf_turbo_all_long_robust1.sh
bash bash_run/run_tf_turbo_all_short_robust1.sh

bash bash_run/run_tf_gpt4_all_long_robust2.sh
bash bash_run/run_tf_gpt4_all_short_robust2.sh
bash bash_run/run_tf_text3_all_long_robust2.sh
bash bash_run/run_tf_text3_all_short_robust2.sh
bash bash_run/run_tf_turbo_all_long_robust2.sh
bash bash_run/run_tf_turbo_all_short_robust2.sh

bash bash_run/run_tf_gpt4_all_long_robust3.sh
bash bash_run/run_tf_gpt4_all_short_robust3.sh
bash bash_run/run_tf_text3_all_long_robust3.sh
bash bash_run/run_tf_text3_all_short_robust3.sh
bash bash_run/run_tf_turbo_all_long_robust3.sh
bash bash_run/run_tf_turbo_all_short_robust3.sh




# unrun


api lack 有问题！！！需要删掉了重来！！
api update也有问题！

# rerun

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15

avg api cost: 9.65625
avg_token_costs: 11724.75
string acc: 60/160=0.375
position acc: 2/21=0.09523809523809523

none

avg api cost: 9.9125
avg_token_costs: 9360.4875
string acc: 45/160=0.28125
position acc: 2/21=0.09523809523809523

avg api cost: 4.585558252427185
avg_token_costs: 4173.515169902913
string acc: 968/1648=0.587378640776699
position acc: 60/282=0.2127659574468085

avg api cost: 11.40625
avg_token_costs: 9229.78125
string acc: 56/160=0.35
position acc: 3/21=0.14285714285714285

none

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --noisy 
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --noisy
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --noisy

avg api cost: 9.225
avg_token_costs: 11539.3625
string acc: 55/160=0.34375
position acc: 2/21=0.09523809523809523

none

avg api cost: 10.975
avg_token_costs: 10335.1125
string acc: 39/160=0.24375
position acc: 4/21=0.19047619047619047

avg api cost: 4.581917475728155
avg_token_costs: 4655.002427184466
string acc: 806/1648=0.4890776699029126
position acc: 55/282=0.1950354609929078

avg api cost: 11.44375
avg_token_costs: 8747.7125
string acc: 50/160=0.3125
position acc: 4/21=0.19047619047619047

none

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0

avg api cost: 8.90625
avg_token_costs: 12597.04375
string acc: 51/160=0.31875
position acc: 3/21=0.14285714285714285

none

avg api cost: 14.61875
avg_token_costs: 10027.56875
string acc: 34/160=0.2125
position acc: 1/21=0.047619047619047616

avg api cost: 4.556432038834951
avg_token_costs: 4166.4429611650485
string acc: 876/1648=0.5315533980582524
position acc: 56/282=0.19858156028368795

avg api cost: 12.0875
avg_token_costs: 9002.4
string acc: 44/160=0.275
position acc: 2/21=0.0952380952380952

none

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1

avg api cost: 9.2625
avg_token_costs: 12021.7375
string acc: 48/160=0.3
position acc: 3/21=0.14285714285714285

none

avg api cost: 12.25625
avg_token_costs: 9461.2
string acc: 28/160=0.175
position acc: 1/21=0.047619047619047616

avg api cost: 4.819781553398058
avg_token_costs: 4169.30036407767
string acc: 851/1648=0.5163834951456311
position acc: 55/282=0.1950354609929078

avg api cost: 12.3
avg_token_costs: 9420.075
string acc: 46/160=0.2875
position acc: 2/21=0.09523809523809523

none

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2

avg api cost: 8.925
avg_token_costs: 12001.35
string acc: 49/160=0.30625
position acc: 3/21=0.14285714285714285

none

avg api cost: 10.46875
avg_token_costs: 9169.5625
string acc: 35/160=0.21875
position acc: 2/21=0.09523809523809523

avg api cost: 4.546723300970874
avg_token_costs: 4196.040655339806
string acc: 846/1648=0.5133495145631068
position acc: 53/282=0.1879432624113475

avg api cost: 12.46875
avg_token_costs: 9561.975
string acc: 54/160=0.3375
position acc: 3/21=0.14285714285714285

none

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3

avg api cost: 10.06875
avg_token_costs: 12810.1625
string acc: 54/160=0.3375
position acc: 4/21=0.19047619047619047

none

avg api cost: 13.03125
avg_token_costs: 9539.80625
string acc: 34/160=0.2125
position acc: 2/21=0.09523809523809523

avg api cost: 4.463592233009709
avg_token_costs: 4195.7597087378645
string acc: 843/1648=0.5115291262135923
position acc: 53/282=0.1879432624113475

avg api cost: 11.56875
avg_token_costs: 9292.1125
string acc: 52/160=0.325
position acc: 2/21=0.09523809523809523

none



python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
none
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
none

python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3


# torun
bash bash_run/run_tf_gpt4_all_long_lack.sh
bash bash_run/run_tf_gpt4_all_short_lack.sh
bash bash_run/run_tf_text3_all_long_lack.sh
bash bash_run/run_tf_text3_all_short_lack.sh
bash bash_run/run_tf_turbo_all_long_lack.sh
bash bash_run/run_tf_turbo_all_short_lack.sh

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 9.225
avg_token_costs: 11842.5875
string acc: 3/160=0.01875
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_lack
none
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 10.54375
avg_token_costs: 9409.63125
string acc: 3/160=0.01875
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_lack 
none
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 11.5125
avg_token_costs: 9242.94375
string acc: 4/160=0.025
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_lack
none

bash bash_run/run_tf_gpt4_all_long_update.sh
bash bash_run/run_tf_gpt4_all_short_update.sh
bash bash_run/run_tf_text3_all_long_update.sh
bash bash_run/run_tf_text3_all_short_update.sh
bash bash_run/run_tf_turbo_all_long_update.sh
bash bash_run/run_tf_turbo_all_short_update.sh

python main.py --eval --dataset=long --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
avg api cost: 8.76875
avg_token_costs: 11673.75625
string acc: 39/160=0.24375
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
none
python main.py --eval --dataset=long --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update
avg api cost: 8.93125
avg_token_costs: 9453.89375
string acc: 27/160=0.16875
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update 
none
python main.py --eval --dataset=long --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update
String correct : 0
avg api cost: 11.33125
avg_token_costs: 9165.00625
string acc: 37/160=0.23125
position acc: 1/21=0.047619047619047616
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update
none

bash bash_run/run_sess_gpt4_all_long_lack.sh
bash bash_run/run_sess_gpt4_all_short_lack.sh
bash bash_run/run_sess_text3_all_long_lack.sh
bash bash_run/run_sess_text3_all_short_lack.sh
bash bash_run/run_sess_turbo_all_long_lack.sh
bash bash_run/run_sess_turbo_all_short_lack.sh

python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 30.32
avg_token_costs: 38554.14
string acc: 0/50=0.0
position acc: 2/20=0.1
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_lack
none
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 38.1
avg_token_costs: 31213.4
string acc: 0/50=0.0
position acc: 2/20=0.1
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_lack 
none
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_lack
avg api cost: 34.56
avg_token_costs: 30394.18
string acc: 0/50=0.0
position acc: 2/20=0.1
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_lack
none

bash bash_run/run_sess_gpt4_all_long_update.sh
bash bash_run/run_sess_gpt4_all_short_update.sh
bash bash_run/run_sess_text3_all_long_update.sh
bash bash_run/run_sess_text3_all_short_update.sh
bash bash_run/run_sess_turbo_all_long_update.sh
bash bash_run/run_sess_turbo_all_short_update.sh

python main.py --eval --dataset=long --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
avg api cost: 30.48
avg_token_costs: 38266.8
string acc: 1/50=0.02
position acc: 2/20=0.1
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --api_update
none
python main.py --eval --dataset=long --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update
avg api cost: 30.48
avg_token_costs: 30590.22
string acc: 0/50=0.0
position acc: 1/20=0.05
python main.py --eval --dataset=short --sess --model=turbo --api_selection --planning --content_selection --api_topk=15 --api_update 
none
python main.py --eval --dataset=long --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update
avg api cost: 36.98
avg_token_costs: 30000.54
string acc: 0/50=0.0
position acc: 1/20=0.05
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --api_update
none

bash bash_run/run_tf_text3_all_short.sh
bash bash_run/run_tf_gpt4_all_short.sh
bash bash_run/run_sess_gpt4_all_short.sh
bash bash_run/run_tf_text3_all_short_noisy.sh
bash bash_run/run_tf_gpt4_all_short_noisy.sh
bash bash_run/run_tf_text3_all_short_robust0.sh
bash bash_run/run_tf_gpt4_all_short_robust0.sh
bash bash_run/run_sess_text3_all_short_robust0.sh
bash bash_run/run_sess_gpt4_all_short_robust0.sh
bash bash_run/run_tf_text3_all_short_robust1.sh
bash bash_run/run_tf_gpt4_all_short_robust1.sh
bash bash_run/run_sess_text3_all_short_robust1.sh
bash bash_run/run_tf_text3_all_short_robust2.sh
bash bash_run/run_tf_gpt4_all_short_robust2.sh
bash bash_run/run_tf_text3_all_short_robust3.sh
bash bash_run/run_tf_gpt4_all_short_robust3.sh

python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15
avg api cost: 5.091626213592233
avg_token_costs: 4602.690533980583
string acc: 784/1648=0.47572815533980584
position acc: 59/282=0.20921985815602837
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15
none
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15
avg api cost: 29.23580786026201
avg_token_costs: 33466.576419213976
string acc: 12/229=0.05240174672489083
position acc: 18/154=0.11688311688311688
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --noisy
none
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --noisy
none
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
none
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
none
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
avg api cost: 42.86899563318777
avg_token_costs: 37966.02183406113
string acc: 1/229=0.004366812227074236
position acc: 14/154=0.09090909090909091
python main.py --eval --dataset=short --sess --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=0
avg api cost: 31.323144104803493
avg_token_costs: 35921.44978165939
string acc: 4/229=0.017467248908296942
position acc: 15/154=0.09740259740259741
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
none
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
none
python main.py --eval --dataset=short --sess --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=1
none
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
none
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=2
none
python main.py --eval --dataset=short --tf --model=text3 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
none
python main.py --eval --dataset=short --tf --model=gpt4 --api_selection --planning --content_selection --api_topk=15 --robust --robust_num=3
none


You can put this into a batch file or script to run them sequentially.

none tf text3 short -> bash bash_run/run_tf_text3_all_short_none.sh
none tf gpt4 short
none sess gpt4 short
noisy tf text3 short
noisy tf gpt4 short
robust0 tf text3 short
robust0 tf gpt4 short
robust0 sess text3 short
robust0 sess gpt4 short
robust1 tf text3 short
robust1 tf gpt4 short
robust1 sess text3 short
robust2 tf text3 short
robust2 tf gpt4 short
robust3 tf text3 short
robust3 tf gpt4 short


